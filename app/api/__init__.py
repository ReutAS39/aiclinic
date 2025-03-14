from fastapi import APIRouter

from .views import router

router = APIRouter()
router.include_router(router=router)