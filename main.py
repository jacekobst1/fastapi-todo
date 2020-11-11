from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


app = FastAPI(title="Todo API")

todos = []


@app.get('/todos', response_model=List[Todo])
async def index():
    return todos


@app.post('/todos')
async def create(todo: Todo):
    todos.append(todo)
    return todo


@app.get('/todos/{item_id}')
async def show(item_id: int):
    try:
        return todos[item_id]
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.put('/todos/{item_id}')
async def update(item_id: int, item: Todo):
    try:
        todos[item_id] = item
        return todos[item_id]
    except:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete('/todos/{item_id}')
async def delete(item_id: int):
    try:
        obj = todos[item_id]
        todos.pop(item_id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Item not found")
