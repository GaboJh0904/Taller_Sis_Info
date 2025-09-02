# app/main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.api import auth, users, projects, tools, materials, flow_tools, flow_materials
from fastapi.middleware.cors import CORSMiddleware
from app.api import (auth, users, projects, tools, materials, flow_tools, flow_materials, surplus_project,
                     material_allocation, tool_allocation, used_material, purchases_material, purchase_material_details,
                     purchase_tools, purchase_tool_details, providers)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router, prefix="/users")
app.include_router(projects.router, prefix="/projects")
app.include_router(tools.router, prefix="/tools")
app.include_router(materials.router, prefix="/materials")
app.include_router(flow_tools.router, prefix="/flow-tools")
app.include_router(flow_materials.router, prefix="/flow-materials")
app.include_router(surplus_project.router, prefix="/surpluses")
app.include_router(material_allocation.router, prefix="/material-allocations")
app.include_router(tool_allocation.router, prefix="/tool-allocations")
app.include_router(used_material.router, prefix="/used-materials")
app.include_router(purchases_material.router, prefix="/purchases-materials")
app.include_router(purchase_material_details.router, prefix="/purchase-material-details")
app.include_router(purchase_tools.router, prefix="/purchase-tools")
app.include_router(purchase_tool_details.router, prefix="/purchase-tool-details")
app.include_router(providers.router, prefix="/providers")



from fastapi import FastAPI, WebSocket, Depends
from app.db.connection import get_connection
import asyncio

connected_clients = []
# Lista global para manejar clientes conectados
connected_clients_tools = []


@app.websocket("/ws/material")
async def websocket_material(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            # Consulta y envía datos a los clientes conectados
            async with get_connection() as conn:
                async with conn.cursor() as cursor:
                    query = """
                    SELECT ID, NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA 
                    FROM MATERIAL
                    """
                    await cursor.execute(query)
                    records = await cursor.fetchall()

                    # Formatear los datos
                    data = [
                        {
                            "ID": row[0],
                            "NOMBRE": row[1],
                            "DESCRIPCION": row[2],
                            "CANTIDAD": row[3],
                            "PRECIO_UNITARIO": row[4],
                            "CANTIDAD_MINIMA": row[5],
                        }
                        for row in records
                    ]

                    # Enviar datos a todos los clientes conectados
                    for client in connected_clients:
                        try:
                            await client.send_json(data)
                        except WebSocketDisconnect:
                            connected_clients.remove(client)

            # Espera 3 segundos antes de enviar la siguiente actualización
            await asyncio.sleep(3)

    except WebSocketDisconnect:
        print("Cliente desconectado")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)

@app.websocket("/ws/herramienta")
async def websocket_herramienta(websocket: WebSocket):
    await websocket.accept()
    connected_clients_tools.append(websocket)

    try:
        while True:
            # Consulta y envía datos a los clientes conectados
            async with get_connection() as conn:
                async with conn.cursor() as cursor:
                    query = """
                    SELECT ID, NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA 
                    FROM HERRAMIENTA
                    """
                    await cursor.execute(query)
                    records = await cursor.fetchall()

                    # Formatear los datos
                    data = [
                        {
                            "ID": row[0],
                            "NOMBRE": row[1],
                            "DESCRIPCION": row[2],
                            "CANTIDAD": row[3],
                            "PRECIO_UNITARIO": row[4],
                            "CANTIDAD_MINIMA": row[5],
                        }
                        for row in records
                    ]

                    # Enviar datos a todos los clientes conectados
                    for client in connected_clients_tools:
                        try:
                            await client.send_json(data)
                        except WebSocketDisconnect:
                            connected_clients_tools.remove(client)

            # Espera 3 segundos antes de enviar la siguiente actualización
            await asyncio.sleep(3)

    except WebSocketDisconnect:
        print("Cliente desconectado")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if websocket in connected_clients_tools:
            connected_clients_tools.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)