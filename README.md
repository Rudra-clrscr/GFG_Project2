# Bakery Intelligence Agent 🥐🤖

Welcome to the **Bakery Intelligence Agent** project. This project leverages the **Model Context Protocol (MCP)** and Google's **Agent Development Kit (ADK)** to create a sophisticated AI assistant designed to help entrepreneurs launch and optimize their bakery business.

## 🚀 Overview

This agent acts as a strategic consultant, combining data-driven insights from BigQuery with real-world location intelligence from Google Maps. It's designed to answer complex questions about market entry, competitive analysis, and operational logistics.

## ✨ Key Features

- **Location Intelligence**: Integrated with the **Google Maps MCP Toolset** for competition analysis, finding optimal locations, and route planning.
- **Data-Driven Insights**: Connected to **BigQuery** to analyze demographic data, foot traffic indexes, historical sales, and product pricing within the `mcp_bakery` dataset.
- **State-of-the-art AI**: Powered by **Gemini 3.1 Pro Preview** via the ADK `LlmAgent` framework.
- **Interactive Maps**: The agent can provide hyperlinks to interactive maps for visual context.

## 🛠️ Project Structure

- `mcp/`: Contains the MCP server implementations and core logic.
- `mcp/examples/launchmybakery/`: The primary workspace for the Bakery Intelligence Agent.
- `adk_agent/mcp_bakery_app/`: Contains the agent definition (`agent.py`) and custom tools (`tools.py`).
- `run_bq.ps1`: Helper script for BigQuery operations.

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- Google Cloud Project with BigQuery and Google Maps APIs enabled.
- A `.env` file configured with your credentials.

### Configuration
Create a `.env` file in `mcp/examples/launchmybakery/adk_agent/mcp_bakery_app/` with the following variables:
```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_MAPS_API_KEY=your-api-key
# Add other necessary credentials
```

### Running the Agent
Navigate to the project directory and run the agent:
```powershell
# Commands to run the agent (replace with actual command if different)
python -m adk_agent.mcp_bakery_app.agent
```

## ☁️ Deployment

This project is optimized for deployment on **Google Cloud Run**. You can deploy the agent as a containerized service to provide an always-on intelligence API.

```bash
gcloud run deploy bakery-agent --source .
```

## 📜 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](mcp/LICENSE) file for details.

---
*Created as part of my professional portfolio to demonstrate AI agent development and Google Cloud integration.*
