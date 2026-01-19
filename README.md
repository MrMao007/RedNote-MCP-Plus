# RedNote-MCP-Plus

[![English](https://img.shields.io/badge/English-Click-yellow)](docs/README.en.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![PyPI version](https://badge.fury.io/py/rednote_mcp_plus.svg)](https://badge.fury.io/py/rednote_mcp_plus)

plus version of MCP server for accessing RedNote(XiaoHongShu, xhs).
```
brew install uv
brew install node
pip install playwright
playwright install
```

## MCP Server Config

```
{
  "mcpServers": {
    "RedNote_MCP_Plus": {
      "command": "uvx",
      "args": [
        "rednote_mcp_plus",
        "--stdio"
      ]
    }
  }
}
```

## MCP Inspector

```
npx @modelcontextprotocol/inspector uvx rednote_mcp_plus
```