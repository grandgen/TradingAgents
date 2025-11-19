# adk_trading_agents/agents/fundamentals_analyst.py
from google.adk.agents.llm_agent import LlmAgent
from adk_trading_agents.tools.financial_tools import (
    fundamentals_tool,
    balance_sheet_tool,
    cashflow_tool,
    income_statement_tool,
)

fundamentals_analyst = LlmAgent(
    name="fundamentals_analyst",
    model="gemini-pro-latest",
    instruction="Analyze the fundamental information for the given company and provide a detailed report.",
    tools=[
        fundamentals_tool,
        balance_sheet_tool,
        cashflow_tool,
        income_statement_tool,
    ],
)
