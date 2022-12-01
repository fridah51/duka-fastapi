from fastapi import APIRouter
from .sales import sales_router
from .inventory import products_router
from .stkpush import stkpush_router


router = APIRouter()


router.include_router(sales_router, prefix = "/sales", tags=["SALES"], )
router.include_router(products_router, prefix = "/products", tags=["PRODUCTS"], )
router.include_router(stkpush_router, prefix = "/stkpush", tags=["STKPUSH"], )