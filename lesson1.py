from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import logging
from pydantic import BaseModel
from typing import Optional
import pandas as pd
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


app = FastAPI()

list_task = []

class Tasks(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = True



@app.get('/tasks', response_class=HTMLResponse)
async def all_tasks():
    log.info('отработал запрос GET')
    table_task = pd.DataFrame([vars(task) for task in list_task]).to_html(index=False)
    return table_task


@app.get('/tasks/{id}', response_class=HTMLResponse)
async def all_tasks(id: int ):
    log.info('отработал запрос GET по id')
    if id <= 0:
        log.error('ошибка ID меньше 1')
        message={'error': 'введите id выше нуля '}
        return JSONResponse(content=message, status_code=500)
    try:    
        table_task = pd.DataFrame([vars(list_task[id-1])]).to_html(index=False)
    except (IndexError, AttributeError):
        log.error('ошибка неверный ID')
        message = {'error': 'введен не корректный ID'}
        return  JSONResponse(content=message, status_code=500)
    return table_task
    
@app.put('/tasks/{id}', response_class=HTMLResponse)
async def all_tasks(id: int, task: Tasks ):
    log.info('отработал запрос PUT по id')
    if id <= 0:
        log.error('ошибка ID меньше 1')
        message={'error': 'введите id выше нуля '}
        return JSONResponse(content=message, status_code=500)
    try:
        task.id = id   
        list_task[id-1] = task
        table_task = pd.DataFrame([vars(list_task[id-1])]).to_html(index=False)
    except (IndexError, AttributeError):
        log.error('ошибка неверный ID')
        message = {'error': 'введен не корректный ID'}
        return  JSONResponse(content=message, status_code=500)
    return table_task


@app.post('/tasks/', response_model=Tasks)
async def post_id(task: Tasks):
    log.info('отработал запрос POST')
    task.id = len(list_task) + 1
    list_task.append(task)
    return task

@app.delete('/tasks/{id}')
async def deletes(id: int):
    log.info('отработал запрос delete')
    if id <= 0:
        log.error('ошибка ID меньше 1')
        message={'error': 'введите id выше нуля '}
        return JSONResponse(content=message, status_code=500)
    try:
        list_task.pop(id-1)
        message = {'message_info': 'задача под номером {id} удалена'}
        return JSONResponse(content=message, status_code=200)
    except (IndexError, AttributeError):
        log.error('ошибка неверный ID')
        message = {'error': 'введен не корректный ID'}
        return  JSONResponse(content=message, status_code=500)
    

