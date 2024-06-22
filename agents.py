
# from langchain_groq import ChatGroq

# import os
# from crewai import ChatMistralAI  # Assuming crewai supports a similar structure for Mistral

# llm = ChatMistralAI(
#     model="open-mistral-7b",
#     api_base=os.getenv("OPENAI_API_BASE"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     verbose=True,
#     temperature=0.5
# )
# from crewai import ChatOpenAI  # Assuming crewai uses OpenAI compatible interface

# Set environment variables
# os.environ['OPENAI_API_KEY'] = 'your-mistral-api-key'
# os.environ['OPENAI_API_BASE'] = 'https://api.mistral.ai/v1'
# os.environ['OPENAI_MODEL_NAME'] = 'mistral-small'

# Initialize LLM
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_MODEL_NAME"),
#     api_base=os.getenv("OPENAI_API_BASE"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     verbose=True,
#     temperature=0.5
# )

# Initialize the LLM with the custom model
# Settings.llm = Ollama(model="mistral", request_timeout=60.0)
# from langchain.llms import Ollama

# ollama_openhermes=Ollama(model="agent")
# llm= ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                             verbose=True,
#                             temperature=0.5,
#                             google_api_key=os.getenv("GOOGLE_API_KEY")
#                             )
from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
import os
from getpass import getpass
os.environ["OPENAI_API_KEY"] = "NA"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"

class tripagents():
    def __init__(self):
        self.llm= ChatOpenAI(
        model="llama2",
        base_url="http://localhost:11434/v1",
        # api_key="NA"
    )
    def City_selection_expert(self):
        return Agent(
            role='city selection expert',
            goal='select the best city based on the season,prices,weather and traveler interests',
            verbose=True,
            memory=False,
            backstory=("Expert in analysing travel data to pick the ideal destination"),
            tool=[search_tool],
            llm=self.llm,
            allow_delegation=True
        )       
    def local_tour_guide(self):
        return Agent(
            role='local tour guide',
            goal='knowledgeable local guide with information about its local customs,attractions and the city',
            verbose=True,
            memory=False,
            backstory=("Expert in making decions regarding the local destiantions"),
            tool=[search_tool],
            llm=self.llm,
            allow_delegation=True
    )   
    def expert_travel_agent(self):
        return Agent(
            role='Expert Travel Agent who makes major decisions',
            goal='create a 7 day itinery with detailed per day plans,include budget, packing suggestions and safety tips',
            verbose=True,
            memory=False,
            backstory=("Expert in travel plan and logistics and highly experienced in making travel plans and iteneraries"),
            tool=[search_tool],
            llm=self.llm,
            allow_delegation=False
        )