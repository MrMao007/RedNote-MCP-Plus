from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP()

@mcp.tool()
def hello_world():
    """Simple tool that returns hello world"""
    return "hello world"

if __name__ == "__main__":
    mcp.run(transport='stdio') 