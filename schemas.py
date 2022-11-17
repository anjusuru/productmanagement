from datetime import datetime
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    brand: str
    price: float
    quantity: int
    category: str

    class config:
        orm_mode =True

class Order(BaseModel):
    order_id :int
    quantity : int
    is_active : bool
    date_created : datetime
    date_modified : datetime

    class config:
        orm_mode =True


