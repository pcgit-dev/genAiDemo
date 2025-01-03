import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
import http.client

def get_current_weather():
    """Get cuurent weather"""
    conn = http.client.HTTPSConnection("ai-weather-by-meteosource.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "62f399251cmsh374889f07aa8698p11f41bjsnaf58e6355481",
        'x-rapidapi-host': "ai-weather-by-meteosource.p.rapidapi.com"
    }

    conn.request("GET", "/time_machine?lat=37.81021&lon=-122.42282&date=2021-08-24&units=auto", headers=headers)

        
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

tools = [
  {
      "type": "function",
      "function": {
          "name": "get_current_weather",
          "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
          "additionalProperties": False,
          },
  }
  
]

OpenAI.api_key = os.getenv(key="OPENAI_API_KEY")
print(OpenAI.api_key)

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "user", "content": "Weather Details"},
  
  ],
  tools=tools,

)
print(completion.choices[0].message)

