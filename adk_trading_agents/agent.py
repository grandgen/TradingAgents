# adk_trading_agents/agent.py
import logging
from google.adk.agents import SequentialAgent, ParallelAgent
from adk_trading_agents.agents.fundamentals_analyst import fundamentals_analyst
from adk_trading_agents.agents.bull_researcher import bull_researcher
from adk_trading_agents.agents.bear_researcher import bear_researcher
from adk_trading_agents.agents.trader import trader
from adk_trading_agents.agents.aggresive_debator import aggresive_debator
from adk_trading_agents.agents.conservative_debator import conservative_debator
from adk_trading_agents.agents.neutral_debator import neutral_debator
from adk_trading_agents.agents.risk_manager import risk_manager
from adk_trading_agents.callbacks import All_CALLBACKS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configure logging for verbose output
logging.basicConfig(
    level=logging.INFO, # Set to INFO for a cleaner, high-level trace
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

research_team = ParallelAgent(
    name="research_team", sub_agents=[bull_researcher, bear_researcher]
)

risk_management_team = ParallelAgent(
    name="risk_management_team",
    sub_agents=[aggresive_debator, conservative_debator, neutral_debator],
)

root_agent = SequentialAgent(
    name="trading_team",
    sub_agents=[
        fundamentals_analyst,
        research_team,
        trader,
        risk_management_team,
        risk_manager,
    ],
    callbacks=All_CALLBACKS
)
