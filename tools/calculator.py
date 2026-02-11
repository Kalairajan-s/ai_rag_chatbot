# tools/calculator.py
from langchain.tools import Tool
calculator_tool = Tool(
    name="Calculator",
    func=lambda x: eval(x),
    description="Math operations"
)
