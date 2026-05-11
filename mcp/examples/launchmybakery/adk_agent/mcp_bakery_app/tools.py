import os
import dotenv
import google.auth
import google.auth.transport.requests
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams 

MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp" 
BIGQUERY_MCP_URL = "https://bigquery.googleapis.com/mcp" 

def get_maps_mcp_toolset():
    dotenv.load_dotenv()
    maps_api_key = os.getenv('MAPS_API_KEY', 'no_api_found')
    
    tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MAPS_MCP_URL,
            headers={    
                "X-Goog-Api-Key": maps_api_key
            },
            timeout=30.0,          
            sse_read_timeout=300.0
        )
    )
    print("MCP Toolset configured for Streamable HTTP connection.")
    return tools


def get_bigquery_mcp_toolset():   
    import httpx
    from google.adk.tools.mcp_tool.mcp_session_manager import create_mcp_http_client

    credentials, project_id = google.auth.default(
            scopes=["https://www.googleapis.com/auth/bigquery"]
    )

    async def auth_hook(request):
        if not credentials.valid:
            import google.auth.transport.requests
            credentials.refresh(google.auth.transport.requests.Request())
        request.headers['Authorization'] = f"Bearer {credentials.token}"
        
    def custom_client_factory(*args, **kwargs):
        client = create_mcp_http_client(*args, **kwargs)
        client.event_hooks['request'].append(auth_hook)
        return client

    HEADERS_WITHOUT_OAUTH = {
        "x-goog-user-project": project_id
    }

    tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=BIGQUERY_MCP_URL,
            headers=HEADERS_WITHOUT_OAUTH,
            timeout=30.0,          
            sse_read_timeout=300.0,
            httpx_client_factory=custom_client_factory
        )
    )
    print("MCP Toolset configured for Streamable HTTP connection with dynamic auth.")
    return tools
