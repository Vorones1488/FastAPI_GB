from fastapi import APIRouter
from base_model import OrderTables, database, Users, Product
import model as md
from typing import List
import logging
from fastapi.responses import JSONResponse



logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

router = APIRouter()

@router.post("/order/", response_model=md.OrderTable_out)
async def create_item(order: md.OrderTables_in):
    log.info('отработал запрос POST')
    query_id_user = Users.__table__.select().where(Users.__table__.c.id == order.id_user)
    query_id_product = Product.__table__.select().where(Product.__table__.c.id == order.id_product)
    if await database.fetch_one(query_id_user) and await database.fetch_one(query_id_product):
        query = OrderTables.__table__.insert().values(**order.dict())
        record_id = await database.execute(query)
        return {**order.dict(), 'id': record_id, 'data_order':record_id}
    return JSONResponse({'error': 'id пользователя или товара не найден'})

@router.get('/order/', response_model=List[md.OrderTable_out])
async def reed_order():
    log.info('отработал запрос GET')
    query = OrderTables.__table__.select()
    return await database.fetch_all(query)

@router.get('/order/{id_order}', response_model=md.OrderTable_out)
async def order_id_read(id_order: int):
    log.info('отработал запрос GET')
    query = OrderTables.__table__.select().where(OrderTables.__table__.c.id == id_order)
    return await database.fetch_one(query)


@router.put('/order/{id_order}', response_model=md.OrderTables_in)
async def update_user(id_order: int, order: md.OrderTable_out):
    log.info('отработал запрос PUT')
    query_id_user = Users.__table__.select().where(Users.__table__.c.id == order.id_user)
    query_id_product = Product.__table__.select().where(Product.__table__.c.id == order.id_product)
    if await database.fetch_one(query_id_user) and await database.fetch_one(query_id_product):
        query = OrderTables.__table__.update().where(OrderTables.__table__.c.id == id_order).values(**order.dict())
        await database.execute(query)
        return {**order.dict(), 'id': id_order}
    return JSONResponse({'error': 'id пользователя или товара не найден'})


@router.delete('/order/{id_order}', response_class=JSONResponse)
async def users_delete(id_order: int):
    log.info('отработал запрос Delete')
    query = OrderTables.__table__.delete().where(Users.__table__.c.id == id_order)
    await database.execute(query)
    return{'info': 'Пользователь удален'}