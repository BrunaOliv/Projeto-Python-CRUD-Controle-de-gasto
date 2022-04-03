from msilib.schema import Class
from re import template
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "modelo.html"
