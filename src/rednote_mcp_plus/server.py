from mcp.server.fastmcp import FastMCP
import os

from rednote_mcp_plus.write import publish

mcp = FastMCP()

@mcp.tool()
def hello_world():
    """Simple tool that returns hello world"""
    return "hello world"

if __name__ == "__main__":
    # mcp.run(transport='stdio') 
    publish.publishText(
        image_urls=["src/rednote_mcp_plus/static/images/ball.png"],
        title="这是一个测试标题",
        content="这是一个测试内容",
        tags=["测试", "小红书"]
    )
