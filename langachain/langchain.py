from langchain.llms import OpenAI
from langchain import HuggingFaceHub
from google.colab import userdata
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = userdata.get('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceHub(repo_id="google/flan-t5-large",model_kwargs={"temperature":0})
propmt= PromptTemplate.from_template("I want to open restaurant for {cuisine} food,suggest me some good names?")
chain1 = LLMChain(llm=llm,prompt=propmt,output_key="restaurant_name")

propmt2= PromptTemplate.from_template("Suggest five menu items for  {restaurant_name} with numbering")
chain2 = LLMChain(llm=llm,prompt=propmt2,output_key="menu_items")

chain = SequentialChain(chains=[chain1,chain2],
                        input_variables=['cuisine'],
                        output_variables=['restaurant_name','menu_items'])
print(chain({"cuisine":"Italian"}))
