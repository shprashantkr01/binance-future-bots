# Binance Futures Testnet Trading Bot (Python)

## Overview

This project is a **simplified Python trading bot** built for **Binance USDT-M Futures Testnet** as part of the *Junior Python Developer – Crypto Trading Bot* assessment.

The application provides a clean, reusable structure to:
- Place **Market** and **Limit** orders
- Support both **BUY** and **SELL** sides
- Accept user input via a **CLI**
- Log API requests, responses, and errors
- Handle validation and exceptions gracefully

The focus of this project is **code quality, structure, validation, and logging**, rather than high-frequency or production trading.

---

## Tech Stack

- **Python** 3.x  
- **python-binance** (Binance Futures API wrapper)  
- **python-dotenv** (environment variable management)  

---

## Project Structure

binance-futures-trading-bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── orders.py # Market & Limit order logic
│ ├── validators.py # CLI input validation
│ └── logging_config.py # Logging configuration
│
├── cli.py # CLI entry point
├── README.md
├── requirements.txt
├── bot.log # Market order log
└── limit_order.log # Limit order log


This structure ensures:
- Separation of concerns
- Reusable components
- Easy testing and maintenance

---

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Binance **USDT-M Futures Testnet** account
- Futures Testnet API key & secret

Testnet base URL used:
https://testnet.binancefuture.com


---

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd binance-futures-trading-bot
3. Create & Activate Virtual Environment
Windows (PowerShell)

python -m venv venv
.\venv\Scripts\Activate.ps1
macOS / Linux

python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Environment Variables
Create a .env file in the project root:

BINANCE_API_KEY=your_futures_testnet_api_key
BINANCE_API_SECRET=your_futures_testnet_api_secret
⚠️ Do not commit API keys to GitHub.

How to Run
All commands should be executed from the project root with the virtual environment activated.

Market Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Limit Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
CLI Input Parameters
Argument	Description
--symbol	Trading pair (e.g., BTCUSDT)
--side	BUY or SELL
--type	MARKET or LIMIT
--quantity	Order quantity
--price	Required for LIMIT orders
Output
The CLI prints:

Order request summary

Order response returned by the API

Clear success or failure message

Example:

Order Request Summary
---------------------
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

Order Response
--------------
{}

✅ Order request sent successfully
Logging
All API interactions are logged:

bot.log → Market order attempts

limit_order.log → Limit order attempts

Logs include:

Timestamp

Request parameters

API responses

Error messages (if any)

This helps with debugging and auditability.

Error Handling & Validation
The application validates:

Symbol format (USDT-M only)

Order side (BUY / SELL)

Quantity and price values

It also handles:

Invalid CLI input

Missing parameters

API errors

Network or authentication issues

Errors are logged and displayed clearly to the user.

Known Testnet Limitation
During testing, Binance USDT-M Futures Testnet may occasionally return an empty response ({}) for order placement while still accepting the request.

To ensure correctness:

Connectivity was verified using Futures ping and account endpoints

Authentication was validated independently

Requests and responses are fully logged

This behavior is a known limitation of the Futures Testnet environment and does not reflect production (mainnet) behavior.

Assumptions
The user has a valid Binance Futures Testnet account

API keys are created specifically for Futures Testnet

The project is intended for demonstration and assessment, not live trading

Future Improvements (Optional)
Add Stop-Limit / OCO / TWAP orders

Interactive CLI (menus or prompts)

Mock execution mode for deterministic testing

Unit tests for validation and order logic

Author
Prashant Kumar Sharma
Junior Python Developer – Crypto Trading Bot Assessment