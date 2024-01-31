from fastapi import APIRouter
from base_model import Users, database
import model as md
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import logging
from fastapi.responses import JSONResponse


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

router = APIRouter()


@router.post("/user/", response_model=md.UserOut)
async def create_item(users: md.UserMod):
    log.info('отработал запрос POST')
    users.password = generate_password_hash(users.password)
    query = Users.__table__.insert().values(**users.dict())
    record_id = await database.execute(query)
    return {**users.dict(), 'id': record_id}



@router.get('/user/', response_model=List[md.UserOut])
async def reed_user():
    log.info('отработал запрос GET')
    query = Users.__table__.select()
    return await database.fetch_all(query)

@router.get('/user/{id_user}', response_model=md.UserOut)
async def user_id_read(id_user: int):
    log.info('отработал запрос GET')
    query = Users.__table__.select().where(Users.__table__.c.id == id_user)
    return await database.fetch_one(query)


@router.put('/user/{id_user}', response_model=md.UserOut)
async def update_user(id_user: int, new_users: md.UserMod):
    log.info('отработал запрос PUT')
    new_users.password = generate_password_hash(new_users.password)
    query = Users.__table__.update().where(Users.__table__.c.id == id_user).values(**new_users.dict())
    await database.execute(query)
    return {**new_users.dict(), 'id': id_user}

@router.delete('/user/{id_user}', response_class=JSONResponse)
async def users_delete(id_user: int):
    log.info('отработал запрос Delete')
    query = Users.__table__.delete().where(Users.__table__.c.id == id_user)
    await database.execute(query)
    return{'info': 'Пользователь удален'}