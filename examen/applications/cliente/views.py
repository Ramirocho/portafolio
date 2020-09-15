from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
)
# Create your views here.
# models
from .models import Cliente

class ListAllCliente(ListView):
    template_name = 'cliente/list_all_cliente.html'
    paginate_by = 5
    ordering = 'id'
    model = Cliente



class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/detail_cliente.html"

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        return context
    

class SuccessView(TemplateView):
    template_name = "cliente/success.html"


class ClienteCreateView(CreateView):
    template_name = "cliente/add.html"
    model = Cliente
    fields = ['__all__']
    success_url = reverse_lazy('persona_app:correcto')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cliente/update"
    fields = ['__all__']

