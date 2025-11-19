# adk_trading_agents/tools/financial_tools.py
from adk_trading_agents.tools.alpha_vantage_client import make_api_request
from google.adk.tools import FunctionTool

def get_fundamentals(ticker: str) -> str:
    """
    Retrieve comprehensive fundamental data for a given ticker symbol using Alpha Vantage.
    """
    params = {
        "symbol": ticker,
    }
    return make_api_request("OVERVIEW", params)

fundamentals_tool = FunctionTool(
    func=get_fundamentals,
)

def get_balance_sheet(ticker: str) -> str:
    """
    Retrieve balance sheet data for a given ticker symbol using Alpha Vantage.
    """
    params = {
        "symbol": ticker,
    }
    return make_api_request("BALANCE_SHEET", params)

balance_sheet_tool = FunctionTool(
    func=get_balance_sheet,
)

def get_cashflow(ticker: str) -> str:
    """
    Retrieve cash flow statement data for a given ticker symbol using Alpha Vantage.
    """
    params = {
        "symbol": ticker,
    }
    return make_api_request("CASH_FLOW", params)

cashflow_tool = FunctionTool(
    func=get_cashflow,
)

def get_income_statement(ticker: str) -> str:
    """
    Retrieve income statement data for a given ticker symbol using Alpha Vantage.
    """
    params = {
        "symbol": ticker,
    }
    return make_api_request("INCOME_STATEMENT", params)

income_statement_tool = FunctionTool(
    func=get_income_statement,
)
