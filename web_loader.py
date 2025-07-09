
#CHATTING TO YOUR WEBSITE/BLOG

from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(  # Hugging Face Models or other models
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)  

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://blog.samaltman.com/"  # Paste any URL here
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

# print(docs[0].page_content)
# replace your question(input_variables) with your question 
print(chain.invoke({'question':'Does sam altman ever mention about job Losses due to Artificial Intelligence in this blog ?', 'text':docs[0].page_content}))


# with open("output.txt","w") as file: # For downloading all the contents of site.
#     file.write(docs[0].page_content)