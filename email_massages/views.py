from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from email_massages.forms import EmailMassage, ManagerEmailMassageForm
from email_massages.models import EmailMessage


class EmailMassageListView(LoginRequiredMixin, ListView):
    model = EmailMessage
    template_name = 'email_message/email_list.html'

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class EmailMassageCreateView(LoginRequiredMixin, CreateView):
    model = EmailMessage
    form_class = EmailMassage
    template_name = 'email_message/email_form.html'
    success_url = reverse_lazy('email_massages:email_message_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class EmailMassageUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailMessage
    form_class = EmailMassage
    template_name = 'email_message/email_form.html'

    def get_success_url(self):
        return reverse('email_massages:email_message_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        """
        Функция, определяющая поля для редактирования в зависимости от прав пользователя
        """
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return EmailMassage
        elif user.has_perm('emailmessage.deactivate_emailmessage'):
            return ManagerEmailMassageForm
        else:
            raise PermissionDenied


class EmailMassageDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailMessage
    template_name = 'email_message/email_confirm_delete.html'
    success_url = reverse_lazy('email_massages:email_message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class EmailMassageDetailView(LoginRequiredMixin, DetailView):
    model = EmailMessage
    template_name = 'email_message/email_detaul.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager') and user != self.object.owner:
            raise PermissionDenied
        else:
            return self.object
