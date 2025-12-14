from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    name="Local MCP Server",
    host="127.0.0.1",
    port=8000,
    # stateless_http=True,
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
    mcp.run(transport='sse')
    print("Running Local MCP Server...")