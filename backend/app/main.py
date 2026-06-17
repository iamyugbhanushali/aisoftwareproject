from fastapi import FastAPI

from app.api.agent_routes import router

app = FastAPI()

app.include_router(router)