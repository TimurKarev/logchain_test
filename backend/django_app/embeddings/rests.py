from django_app.services.embeddings import get_embeddings


from django.http import JsonResponse
# 

def some_view(request):

    embedding = get_embeddings()
    return JsonResponse({'data': str(embedding)})