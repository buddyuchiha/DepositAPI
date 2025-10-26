from fastapi import APIRouter, Depends

from api.dependencies import get_deposits_repository, get_user_repository


utils_router = APIRouter(
    tags=["Utils Endpoints"]
)

@utils_router.get(
    "/clean", 
    summary="Clean All", 
    tags=["Utils Endpoints"])
async def clean_all(
    user_db=Depends(get_deposits_repository),
    deposits_db=Depends(get_user_repository)
    ):
    await user_db.clean()
    await deposits_db.clean()
    
    return True