# app/main.py
from fastapi import FastAPI
from app.api import auth, users, projects, tools, materials, flow_tools, flow_materials
from fastapi.middleware.cors import CORSMiddleware
from app.api import (auth, users, projects, tools, materials, flow_tools, flow_materials, surplus_project,
                     material_allocation, tool_allocation, used_material, purchases_material, purchase_material_details,
                     purchase_tools, purchase_tool_details)

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



from fastapi import FastAPI, WebSocket, Depends
from app.db.connection import get_connection
import asyncio

connected_clients = []


@app.websocket("/ws/material")
async def websocket_material(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            # Envía los datos de la tabla MATERIAL a todos los clientes conectados
            async with get_connection() as conn:
                async with conn.cursor() as cursor:
                    query = "SELECT ID, NOMBRE, DESCRIPCION, CANTIDAD, PRECIO_UNITARIO, CANTIDAD_MINIMA FROM MATERIAL"
                    await cursor.execute(query)
                    records = await cursor.fetchall()

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

                    # Envía los datos a cada cliente conectado
                    for client in connected_clients:
                        await client.send_json(data)

            # Espera unos segundos antes de enviar la siguiente actualización
            await asyncio.sleep(3)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connected_clients.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)