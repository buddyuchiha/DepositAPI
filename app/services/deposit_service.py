from schemas.deposits import InputCalculateDepositScheme


async def _calculate_deposit(data: InputCalculateDepositScheme):
    sum = data.amount
    result_dict = {}
    
    for period in range(data.periods): 
        sum = sum * (1 + (data.rate/12*100))
        result_dict[str(period)] = round(sum)
    
    return result_dict 