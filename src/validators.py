def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M symbols supported")
    return symbol

def validate_side(side):
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_quantity(quantity):
    qty = float(quantity)
    if qty <= 0:
        raise ValueError("Quantity must be positive")
    return qty

def validate_price(price):
    p = float(price)
    if p <= 0:
        raise ValueError("Price must be positive")
    return p
