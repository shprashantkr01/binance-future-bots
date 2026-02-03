import argparse
from bot.validators import *
from bot.orders import *
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    logger = setup_logger(
        "bot.log" if args.type == "MARKET" else "limit_order.log"
    )

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        quantity = validate_quantity(args.quantity)

        print("\nOrder Request Summary")
        print("---------------------")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {quantity}")

        if args.type == "MARKET":
            response = place_market_order(symbol, side, quantity)

        else:
            if not args.price:
                raise ValueError("Price is required for LIMIT orders")

            price = validate_price(args.price)
            print(f"Price    : {price}")

            response = place_limit_order(symbol, side, quantity, price)

        logger.info(f"Order request: {vars(args)}")
        logger.info(f"Order response: {response}")

        print("\nOrder Response")
        print("--------------")
        print(response)

        print("\n Order request sent successfully")

    except Exception as e:
        logger.error(str(e))
        print("\n Error:", e)

if __name__ == "__main__":
    main()
