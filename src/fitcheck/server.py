from mcp.server import MCPServer

mcp = MCPServer("Fitcheck")

@mcp.tool()
def ping(name : str ) -> str :
    """a ping tool , use it to check if the mcp server is healthy """
    return(f"hello {name}")


