from pydantic import BaseModel, Field, EmailStr, PastDatetime


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
    id_product: int
    id_user: int
    status_order: bool = Field(default=True)
    
class OrderTable_out(BaseModel):
    id: int
    id_user: int
    id_product: int
    data: str
    status_order: bool = Field(default=True)


class Product_in(BaseModel):
    name_product: str = Field(..., max_length=20)
    descript: str = Field(..., title="description product")
    price:float = Field(..., gt=0)

class Product_in(BaseModel):
    id: int
    name_product: str = Field(..., max_length=20)
    descript: str = Field(..., title="description product")
    price:float = Field(..., gt=0)