from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the model
model = HfApiModel()

agent = CodeAgent(
    model=model,
    tools=[search_tool],
)

# Example usage
response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)
print(response)