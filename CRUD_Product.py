from fastapi import APIRouter
from base_model import Product, database
import model as md
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
import logging
from fastapi.responses import JSONResponse


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

router = APIRouter()

@router.post("/product/", response_model=md.Product_out)
async def create_item(product: md.Product_in):
    log.info('отработал запрос POST')
    query = Product.__table__.insert().values(**product.dict())
    record_id = await database.execute(query)
    return {**product.dict(), 'id': record_id}


@router.get('/product/', response_model=List[md.Product_out])
async def reed_product():
    log.info('отработал запрос GET')
    query = Product.__table__.select()
    return await database.fetch_all(query)

@router.get('/product/{id_product}', response_model=md.Product_out)
async def product_id_read(id_product: int):
    log.info('отработал запрос GET')
    query = Product.__table__.select().where(Product.__table__.c.id == id_product)
    return await database.fetch_one(query)

@router.put('/product/{id_product}', response_model=md.Product_out)
async def update_product(id_product: int, new_product: md.Product_in):
    log.info('отработал запрос PUT')
    query = Product.__table__.update().where(Product.__table__.c.id == id_product).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), 'id': id_product}

@router.delete('/product/{id_product}', response_class=JSONResponse)
async def users_delete(id_product: int):
    log.info('отработал запрос Delete')
    query = Product.__table__.delete().where(Product.__table__.c.id == id_product)
    await database.execute(query)
    return{'info': 'Продукт удален'}