from fastapi import FastAPI

from endpoints import router

app = FastAPI(title="ASCII Art API")

app.include_router(router)
