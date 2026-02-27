
from database import delete_tables, create_tables

from fastapi import Depends, FastAPI

from contextlib import asynccontextmanager
from router import router as tasks_router

items = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Clear base")
    await create_tables()
    print("ON")
    yield
    print("OFF")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


tasks = []



