from fastapi import APIRouter, Depends, HTTPException

from api.dependencies import get_deposits_repository
from schemas.deposits import (
    DefaultDepositScheme,
    InputCalculateDepositScheme, 
    OutputCalculateDepositScheme
    )   
from services.deposit_service import _calculate_deposit


deposits_router = APIRouter(
    tags=["Deposits Endpoints"]
)

@deposits_router.post(
    "/deposits", 
    summary="Create Deposit", 
    tags=["Deposits Endpoints"])
async def create_deposit(
    data: DefaultDepositScheme, 
    db=Depends(get_deposits_repository)
    ):
    return await db.create(data)

@deposits_router.get(
    "/deposits", 
    summary="Get Deposits", 
    tags=["Deposits Endpoints"])
async def get_deposits(
    db=Depends(get_deposits_repository)
    ):
    return await db.get()

@deposits_router.get(
    "/deposits/{deposit_id}", 
    summary="Get Deposit", 
    tags=["Deposits Endpoints"])
async def get_deposit(
    deposit_id: int,     
    db=Depends(get_deposits_repository)
    ):
    return await db.get_single(deposit_id)

@deposits_router.put(
    "/deposits/{deposit_id}", 
    summary="Update Deposit", 
    tags=["Deposits Endpoints"])
async def update_deposit(
    deposit_id: int, 
    data: DefaultDepositScheme, 
    db=Depends(get_deposits_repository)    
    ):
    return await db.update(deposit_id, data)

@deposits_router.delete(
    "/deposits/{deposit_id}", 
    summary="Delete Deposit", 
    tags=["Deposits Endpoints"])
async def delete_deposit(
    deposit_id: int, 
    db=Depends(get_deposits_repository)    
    ):
    return await db.delete(deposit_id)

@deposits_router.post(
  "/calculate-deposit",
  summary="Calculate Deposit",
  response_model=OutputCalculateDepositScheme,
  tags=["Deposits Endpoints"]) 
async def calculate_deposit(
    data: InputCalculateDepositScheme
    ):
    return await _calculate_deposit(data)