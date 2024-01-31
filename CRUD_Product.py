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

@router.post("/user/", response_model=md.UserOut)
async def create_item(users: md.UserMod):
    log.info('отработал запрос POST')
    users.password = generate_password_hash(users.password)
    query = Users.__table__.insert().values(**users.dict())
    record_id = await database.execute(query)
    return {**users.dict(), 'id': record_id}
