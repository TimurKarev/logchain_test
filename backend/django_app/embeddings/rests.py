import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from django_app.services.embeddings import get_embeddings
from django.http import HttpRequest, JsonResponse
from django.views import View

from embeddings.models.embedding_model import EmbeddingModel


@method_decorator(csrf_exempt, name='dispatch')
class EmbeddingsRest(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        body = json.loads(request.body)

        # if (len(body) > 0):
        #     embedding = get_embeddings(post_txt=body)

        return JsonResponse({'data': request.body.data})
