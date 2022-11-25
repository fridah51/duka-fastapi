from fastapi import APIRouter
from .sales import sales_router
from .inventory import products_router



router = APIRouter()


router.include_router(sales_router, prefix = "/sales", tags=["SALES"], )
router.include_router(products_router, prefix = "/products", tags=["PRODUCTS"], )