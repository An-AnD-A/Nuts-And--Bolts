from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    name="Local MCP Server",
    host="0.0.0.0",
    port=8050,
    stateless_http=True,
)


@mcp.tool()
def echo(message: str) -> str:
    """
    Echoes the input message back to the user.
    
    Args:
        message (str): The message to echo.
    
    Returns:
        str: The echoed message.
    """
    return f"Echo: {message}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
    print("Running Local MCP Server...")