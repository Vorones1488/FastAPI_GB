from fastapi import FastAPI
from CRUD_User import router as user_router
from CRUD_Product import router as product_router
from CRUD_OrderTables import router as order_router
from base_model import database
# from base_model import Users, Product, OrderTables
# from datetime import datetime
# from werkzeug.security import generate_password_hash


app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)


# для добавления тест пользователей раскоментировать все строки
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         pass_hesh = generate_password_hash(f'pass{i}')
#         query = Users.__table__.insert().values(name=f'user{i}',
#         email=f'mail{i}@mail.ru',  family = f'famili{i}', password = pass_hesh)
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}

# @app.get("/fake_product/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         price = round(((i+1) * 3.3), 2)
#         query = Product.__table__.insert().values(name_product=f'prod{i}',
#         descript=f'descrip{i}',  price=f'{price}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}

# @app.get("/fake_order/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         id_use = i +2
#         id_prod = i + 1
#         query = OrderTables.__table__.insert().values(id_product=id_prod,
#         id_user=id_use, data_order = datetime.now())
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}