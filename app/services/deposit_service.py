from schemas.deposits import InputCalculateDepositScheme


async def _calculate_deposit(data: InputCalculateDepositScheme):
    sum = data.amount
    dict = {}
    
    async for period in range(data.periods): 
        sum += await period * (1 + (data.rate/12*100))
        dict[period] = sum
    
    return dict 