from fastapi import APIRouter
from app.api.db.base import ProductCreate,ProductCreateSuccessResponse,ListProductsSuccessResponse,ListUsersSuccessResponse

# Roteador para gerenciamento de produtos
router_products = APIRouter(
    prefix="/products",
    tags=["Produtos"],

)
@router_products.post("/add_product", response_model=ProductCreateSuccessResponse, status_code=201)
async def add_product(product_in: ProductCreate = Body(...)):
    """
    Adiciona um novo produto ao estoque.
    Corresponde à tela 'Adicionar Produto'.
    """
    # Lógica para salvar o produto no banco de dados aqui.
    pass

@router_products.get("/list_product", response_model=ListProductsSuccessResponse,status_code=201)
async def list_products():
    """
    Retorna a lista de todos os produtos cadastrados.
    Corresponde à lista 'Estoque' no painel administrativo.
    """
    # Lógica para buscar os produtos no banco de dados aqui.
    pass