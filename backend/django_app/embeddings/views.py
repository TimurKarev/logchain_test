from django.views.generic.base import TemplateView

from embeddings.models.embedding_model import EmbeddingModel
# Create your views here.

class InputDocumentView(TemplateView):
    template_name = 'input_document.html'

    def get(self, request, *args, **kwargs):
        
        return self.render_to_response(super().get_context_data(**kwargs))




