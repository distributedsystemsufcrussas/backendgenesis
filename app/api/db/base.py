from pydantic import BaseModel, EmailStr, Field, List
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., example="Smartphone Pro Max", description="Product name")  # not null
    category: str = Field("OTHER", example="Electronics", description="Product category")  # not null, default
    price: float = Field(..., gt=0, example=2999.99, description="Unit price of the product")  # not null
    stock: int = Field(0, ge=0, example=1, description="Quantity in stock")  # not null, default 0
    description: Optional[str] = Field(None, example="A high-end smartphone with OLED display", description="Product description")  # nullable
    class Config:
        orm_mode = True
class UserBase(BaseModel):
    id: int = Field(..., description="Primary key")
    name: str = Field(..., max_length=255, example="Admin Sistema", description="User full name - not null")
    email: EmailStr = Field(..., example="admin@sistema.com", description="User email - unique, not null")
    phone: Optional[str] = Field(None, max_length=20, example="(11) 99999-9999", description="User phone - unique, not null")
    created_at: datetime = Field(..., example="2024-01-15T10:30:00", description="Creation timestamp - not null")
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
class ProductCreateSuccessResponse(ProductBase):
    pass
class ListProductsSuccessResponse(BaseModel):
    status: str = Field(..., example="success")
    products: List[ProductBase]
    message: str = Field(..., example="Produtos listados com sucesso!")
class ListUsersSuccessResponse(BaseModel):
    status: str = Field(..., example="success")
    products: List[UserBase]
    message: str = Field(..., example="Usuários listados com sucesso!")
