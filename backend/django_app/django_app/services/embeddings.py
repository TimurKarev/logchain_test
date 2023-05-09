from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.callbacks import get_openai_callback

from django_app.domain.models.token_cost_model import TokenCostModel

from keys import openApiKey

#-> List[float] , TokenCostModel
def get_embeddings(post_txt : str):
   embedding_model = OpenAIEmbeddings(openai_api_key=openApiKey)
   cost = TokenCostModel()
   with get_openai_callback() as openai:
      embedding = embedding_model.embed_query(post_txt)
      cost = TokenCostModel(
         total_tokens=openai.total_tokens,
         prompt_tokens=openai.prompt_tokens,
         completion_tokens=openai.completion_tokens,
         successful_requests=openai.successful_requests,
         total_cost=openai.total_cost,
      )

   
   return (embedding, cost)
