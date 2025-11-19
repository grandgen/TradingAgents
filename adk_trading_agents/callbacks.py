# adk_trading_agents/callbacks.py
import logging
from typing import Any

logger = logging.getLogger(__name__)

def before_agent_callback(
    *,
    agent: Any,
    session: Any,
    **kwargs: Any,
) -> None:
    """Called when an agent is about to start."""
    logger.info(f"--- Starting Agent: {agent.name} ---")

def after_agent_callback(
    *,
    agent: Any,
    session: Any,
    **kwargs: Any,
) -> None:
    """Called when an agent has just finished."""
    logger.info(f"--- Finished Agent: {agent.name} ---")

def before_llm_callback(
    *,
    agent: Any,
    session: Any,
    llm_request: Any,
    **kwargs: Any,
) -> None:
    """Called when an LLM call is about to start."""
    logger.info(f"--- Calling LLM for Agent: {agent.name} ---")
    logger.debug(f"LLM Request for {agent.name}: {llm_request}")

def after_llm_callback(
    *,
    agent: Any,
    session: Any,
    llm_response: Any,
    **kwargs: Any,
) -> None:
    """Called when an LLM call has just finished."""
    logger.info(f"--- LLM call finished for Agent: {agent.name} ---")
    logger.debug(f"LLM Response for {agent.name}: {llm_response}")

def before_tool_callback(
    *,
    agent: Any,
    session: Any,
    tool_input: Any,
    **kwargs: Any,
) -> None:
    """Called when a tool is about to be called."""
    tool_name = tool_input.get("name", "Unknown tool")
    logger.info(f"--- Agent {agent.name} is calling Tool: {tool_name} ---")
    logger.debug(f"Tool input: {tool_input}")

def after_tool_callback(
    *,
    agent: Any,
    session: Any,
    tool_output: Any,
    **kwargs: Any,
) -> None:
    """Called when a tool call has just finished."""
    tool_name = tool_output.get("name", "Unknown tool")
    logger.info(f"--- Tool call finished for Agent: {agent.name} ---")
    logger.debug(f"Tool output: {tool_output}")

All_CALLBACKS = {
    "before_agent_callback": before_agent_callback,
    "after_agent_callback": after_agent_callback,
    "before_llm_callback": before_llm_callback,
    "after_llm_callback": after_llm_callback,
    "before_tool_callback": before_tool_callback,
    "after_tool_callback": after_tool_callback,
}
