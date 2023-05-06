from langchain.embeddings.openai import OpenAIEmbeddings
from keys import openApiKey


def get_embeddings() -> OpenAIEmbeddings:
   doc_embedding = OpenAIEmbeddings(openai_api_key=openApiKey)
   return doc_embedding
