from langchain.agents import AgentType, initialize_agent,load_tools
from langchain.llms import OpenAI
from wikipedia import search
import os
os.environ['OPEN_API_KEY'] = userdata.get('OPEN_API_KEY')
llm=OpenAI(openai_api_key=os.environ['OPEN_API_KEY'],temperature=0)
#tools = load_tools(["serpapi","llm-math"],llm=llm

tools = load_tools(["wikipedia","llm-math"],llm=llm)
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
agent.run("What is population of India in 2025")