from fastapi import APIRouter, Depends

from api.dependencies import get_user_repository
from schemas.users import DefaultUserScheme


users_router = APIRouter(
    tags=["Users Endpoints"]
)


@users_router.post(
    "/users", 
    summary="Create User", 
    tags=["Users Endpoints"])
async def create_user(
    data: DefaultUserScheme,
    db=Depends(get_user_repository)
    ):
    return await db.create(data)
    
@users_router.get(
    "/users",
    summary="Get Users", 
    tags=["Users Endpoints"])
async def get_users(db=Depends(get_user_repository)):
    return await db.get()

@users_router.get(
    "/users/{user_id}",
    summary="Get User", 
    tags=["Users Endpoints"])
async def get_user(user_id: int, db=Depends(get_user_repository)):
    return await db.get_single(user_id) 

@users_router.put(
    "/users/{user_id}",
    summary="Put User", 
    tags=["Users Endpoints"])    
async def update_user(
    user_id: int, 
    data: DefaultUserScheme,
    db=Depends(get_user_repository)
    ):
    return await db.update(user_id, data)

@users_router.delete(
    "/users/{user_id}",
    summary="Delete User", 
    tags=["Users Endpoints"])
async def delete_user(user_id: int, db=Depends(get_user_repository)):
    return await db.delete(user_id)