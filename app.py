import os
import chainlit as cl
from typing import List
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import (ConversationalRetrievalChain, ) 
from langchain.memory import ConversationBufferMemory, ChatMessageHistory
from langchain.docstore.document import Document

print('all-ok')


# Loading openai api key from .env
load_dotenv() 

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]= OPENAI_API_KEY

# splitting documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)