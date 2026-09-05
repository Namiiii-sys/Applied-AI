from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first nnumber to add")
    b: int = Field(required=True, description="The second number to add")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a*b
    
    Multiply_tool = MultiplyTool()
 
    result = Multiply_tool.invoke({'a':3,'b':3})

    print(result)
    print(Multiply_tool.name)