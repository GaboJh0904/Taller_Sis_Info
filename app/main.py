# app/main.py
from fastapi import FastAPI
from app.api import auth, users, projects, tools, materials, flow_tools, flow_materials

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router, prefix="/users")
app.include_router(projects.router, prefix="/projects")
app.include_router(tools.router, prefix="/tools")
app.include_router(materials.router, prefix="/materials")
app.include_router(flow_tools.router, prefix="/flow-tools")
app.include_router(flow_materials.router, prefix="/flow-materials")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)