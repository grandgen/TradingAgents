# ADK Trading Agents

This project is a reimplementation of the TradingAgents framework using the Google Agent Development Kit (ADK).

## Running the Agents

To run an agent, use the `adk` command-line interface. For example, to run the `fundamentals_analyst`:

```bash
adk run . --request "Analyze the fundamentals of NVDA"
```

You will need to have your `ALPHA_VANTAGE_API_KEY` and `GOOGLE_API_KEY` environment variables set.
