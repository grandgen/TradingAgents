# adk_trading_agents/callbacks.py
import logging
from google.adk.callbacks import BaseCallback, PrintCallback
from google.adk.sessions import Session
from typing import Any

logger = logging.getLogger(__name__)

class AgentLifecycleLogger(BaseCallback):
    """A callback that logs the start and end of each agent's execution."""

    def on_agent_start(
        self,
        *,
        agent: Any,
        session: Session,
        **kwargs: Any,
    ) -> None:
        """Called when an agent is about to start."""
        logger.info(f"--- Starting Agent: {agent.name} ---")

    def on_agent_end(
        self,
        *,
        agent: Any,
        session: Session,
        **kwargs: Any,
    ) -> None:
        """Called when an agent has just finished."""
        logger.info(f"--- Finished Agent: {agent.name} ---")

    def on_llm_start(
        self,
        *,
        agent: Any,
        session: Session,
        llm_request: Any,
        **kwargs: Any,
    ) -> None:
        """Called when an LLM call is about to start."""
        logger.info(f"--- Calling LLM for Agent: {agent.name} ---")
        # For verbosity, we can log the full prompt at the DEBUG level
        logger.debug(f"LLM Request for {agent.name}: {llm_request}")

    def on_llm_end(
        self,
        *,
        agent: Any,
        session: Session,
        llm_response: Any,
        **kwargs: Any,
    ) -> None:
        """Called when an LLM call has just finished."""
        logger.info(f"--- LLM call finished for Agent: {agent.name} ---")
        logger.debug(f"LLM Response for {agent.name}: {llm_response}")

    def on_tool_start(
        self,
        *,
        agent: Any,
        session: Session,
        tool_input: Any,
        **kwargs: Any,
    ) -> None:
        """Called when a tool is about to be called."""
        tool_name = tool_input.get("name", "Unknown tool")
        logger.info(f"--- Agent {agent.name} is calling Tool: {tool_name} ---")
        logger.debug(f"Tool input: {tool_input}")

    def on_tool_end(
        self,
        *,
        agent: Any,
        session: Session,
        tool_output: Any,
        **kwargs: Any,
    ) -> None:
        """Called when a tool call has just finished."""
        tool_name = tool_output.get("name", "Unknown tool")
        logger.info(f"--- Tool call finished for Agent: {agent.name} ---")
        logger.debug(f"Tool output: {tool_output}")
