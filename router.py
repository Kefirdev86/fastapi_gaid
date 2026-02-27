
from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from database import new_session, TaskOrm
from schemas import STask, STaskid, STaskAdd

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskid:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}
