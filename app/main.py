# app/main.py
from fastapi import FastAPI
from app.api import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router, prefix="/users")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)