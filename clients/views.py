from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from clients.forms import ClientsForm
from clients.models import Client
from django.views.generic import TemplateView

from email_massages.models import EmailMessage


# Create your views here.


class HomeView(TemplateView):
    template_name = 'clients/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        email_massages = EmailMessage.objects.all()
        client = Client.objects.all()
        context_data['all_email_massages'] = email_massages.count()
        context_data['active_email_messages'] = email_massages.filter(status=EmailMessage.STARTED).count
        context_data['unique_client'] = client.values('email').distinct().count
        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/clients_list.html'

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер отвечающий за отображение клиента
    """
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('clients:clients_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientsForm
    template_name = 'clients/client_form.html'

    def get_success_url(self):
        return reverse('clients:client_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied
