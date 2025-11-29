def cal(odd, pba):
    odd = float(odd)
    pba = float(pba)
    # print("Probability:", pba)  # Debugging print
    
    amt = 100
    odd -= 1  # Ensure we don't divide by zero

    proba = round(pba / 100, 4)
    loss = 1 - proba

    if odd == 0:  # Prevent division by zero
        return 0

    f = ( ( (odd * proba) - (loss) ) / odd)
    return f

# print(cal(2.5,60))