from langchain_core.tools import tool

# 1 - create a function

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

def multiplying(a : int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

@tool
def multiplying(a : int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":3,"b":5})
print(multiply.name) 