# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api import auth, users, projects, tools, materials, flow_tools, flow_materials, stores
from fastapi.middleware.cors import CORSMiddleware
import logging
import traceback

from app.api import (auth, users, projects, tools, materials, flow_tools, flow_materials, surplus_project,
                     material_allocation, tool_allocation, used_material, purchases_material, purchase_material_details,
                     purchase_tools, purchase_tool_details, providers)

from app.api import financial, inventory, projects
app = FastAPI()



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Get stack trace and request details
    error_trace = traceback.format_exc()
    try:
        # Attempt to log the body of the request for debugging
        body = await request.json()
    except Exception as e:
        body = {"error": f"Unable to parse body: {e}"}

    logging.error(f"Validation error:\n{exc}\nRequest body: {body}\nTraceback:\n{error_trace}")
    
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": body,  # Include the invalid body for debugging
        },
    )

# @app.exception_handler(Exception)
# async def custom_exception_handler(request: Request, exc: Exception):
#     # Print the stack trace
#     traceback.print_exc()
#     return JSONResponse(
#         status_code=500,
#         content={"detail": str(exc)},
#     )

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
app.include_router(stores.router, prefix="/stores")

app.include_router(inventory.router)
app.include_router(projects.router)
app.include_router(financial.router)


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