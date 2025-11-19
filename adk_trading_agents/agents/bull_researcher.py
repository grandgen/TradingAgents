# adk_trading_agents/agents/bull_researcher.py
from google.adk.agents.llm_agent import LlmAgent

bull_researcher = LlmAgent(
    name="bull_researcher",
    model="gemini-pro-latest",
    instruction="You are a Bull Analyst advocating for investing in the stock. Your task is to build a strong, evidence-based case emphasizing growth potential, competitive advantages, and positive market indicators. Leverage the provided research and data to address concerns and counter bearish arguments effectively.",
)
