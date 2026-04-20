from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from endpoints import router

load_dotenv()
app = FastAPI(title="ASCII Art API")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
