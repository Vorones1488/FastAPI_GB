from pydantic import BaseModel, Field, EmailStr, condecimal
from datetime import datetime


class UserMod(BaseModel):
    name: str = Field(..., max_length=50)
    family: str = Field(default=None, max_length=50 )
    email: EmailStr = Field(..., max_length= 50)
    password:str = Field(..., max_length= 170)
    

class UserOut(BaseModel):
    id:int = Field(..., title='id_user')
    name:str = Field(..., max_length=50)
    family:str = Field(default=None, max_length=50 )
    email: EmailStr = Field(..., max_length= 50)
    password:str = Field(..., max_length= 170)


class OrderTables_in(BaseModel):
    id_product: int = Field(..., ge=1)
    id_user: int = Field(..., ge=1)
    status_order: bool = Field(default=True)
    data_order: datetime = datetime.now()
    
class OrderTable_out(BaseModel):
    id: int = Field(..., ge=1)
    id_user: int = Field(..., ge=1)
    id_product: int = Field(..., ge=1)
    data_order: datetime
    status_order: bool = Field(..., title='staus order actuale')


class Product_in(BaseModel):
    name_product: str = Field(..., max_length=20)
    descript: str = Field(..., title="description product")
    price: condecimal(max_digits=15, decimal_places=2) = Field(..., gt=0)

class Product_out(BaseModel):
    id: int
    name_product: str = Field(..., max_length=20)
    descript: str = Field(..., title="description product")
    price: condecimal(max_digits=15, decimal_places=2) = Field(..., gt=0)