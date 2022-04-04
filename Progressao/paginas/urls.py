from unicodedata import name
from django.urls import  path
from.views import IndexView, TransacaoCreat, TransacaoList, TransacaoUpdate, TransacaoDelete, listagem

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/transacao', TransacaoCreat.as_view(), name='cadastrar_transacao'),
    path('update/transacao/<int:pk>/', TransacaoUpdate.as_view(), name='update_transacao'),
    path('delete/transacao/<int:pk>/', TransacaoDelete.as_view(), name='delete_transacao'),
    path('list/transacao', listagem, name='list_transacao'),
]