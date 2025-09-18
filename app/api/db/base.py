from pydantic import BaseModel, EmailStr, Field, List
from typing import Optional
class UserBase(BaseModel):
    full_name: str = Field(..., example="Admin Sistema")
    email: EmailStr = Field(..., example="admin@sistema.com")
    phone: Optional[str] = Field(None, example="(11) 99999-9999")

class ProductBase(BaseModel):
    name: str = Field(..., example="Smartphone Pro Max")
    category: str = Field(..., example="Eletrônicos")
    price: float = Field(..., gt=0, example=2999.99)

class ProductCreate(ProductBase):
    pass
class UserCreate(UserBase):
    pass
class ProductCreateSuccessResponse(BaseModel):
    status: str = Field(..., example="success")
    product: ProductBase
    message: str = Field(..., example="Produto adicionado com sucesso!")
class ListProductsSuccessResponse(BaseModel):
    status: str = Field(..., example="success")
    products: List[ProductBase]
    message: str = Field(..., example="Produtos listados com sucesso!")