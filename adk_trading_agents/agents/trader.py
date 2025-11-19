# adk_trading_agents/agents/trader.py
from google.adk.agents.llm_agent import LlmAgent

trader = LlmAgent(
    name="trader",
    model="gemini-pro-latest",
    instruction="You are a trading agent analyzing market data to make investment decisions. Based on your analysis, provide a specific recommendation to buy, sell, or hold. End with a firm decision and always conclude your response with 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**' to confirm your recommendation.",
)
