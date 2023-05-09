import docx2txt
from django.shortcuts import render
from django.views.generic.base import TemplateView

from front.forms.upload_file_form import UploadFileForm

from django_app.services.embeddings import get_embeddings

class DocumentLoaderView(TemplateView):
    template_name = 'document_loader_template.html'

    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        doc_file = request.FILES["file"]
        if doc_file:
            try:
                text = docx2txt.process(doc_file)
                embedding = get_embeddings(post_txt=text)
                
                
                status = 'Success: File uploaded.'
            except Exception as e:
                text = ''
                status = f'Error: {e}'
        else:
            text = ''
            status = 'Error: No file selected.'

        return render(request, self.template_name, {'status': status})
