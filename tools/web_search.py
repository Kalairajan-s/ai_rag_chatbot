# tools/web_search.py
from langchain.tools import Tool
web_search_tool = Tool(
    name="WebSearch",
    func=lambda q: f"Search result for {q}",
    description="Web search"
)
