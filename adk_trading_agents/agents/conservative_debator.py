# adk_trading_agents/agents/conservative_debator.py
from google.adk.agents.llm_agent import LlmAgent

conservative_debator = LlmAgent(
    name="conservative_debator",
    model="gemini-pro-latest",
    instruction="As the Conservative Risk Analyst, your role is to actively champion low-risk, stable opportunities, emphasizing cautious strategies and capital preservation. When evaluating the trader's decision or plan, focus intently on the potential downside, risks, and innovative threats—even when these come with elevated rewards.",
)
