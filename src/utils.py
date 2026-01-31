def validate_order(symbol, side, quantity):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures pairs allowed")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    try:
        quantity = float(quantity)
    except:
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    return quantity
