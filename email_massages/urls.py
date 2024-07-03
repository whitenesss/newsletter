from django.urls import path

from email_massages.views import EmailMassageListView, EmailMassageCreateView, EmailMassageUpdateView, \
    EmailMassageDeleteView, EmailMassageDetailView

app_name = 'email_massages'

urlpatterns = [
    path('', EmailMassageListView.as_view(), name='email_message_list'),
    path('email_message_create', EmailMassageCreateView.as_view(), name='email_message_create'),
    path('email_message_update/<int:pk>/', EmailMassageUpdateView.as_view(), name='email_message_update'),
    path('email_message_delete/<int:pk>/', EmailMassageDeleteView.as_view(), name='email_message_delete'),
    path('email_message_detail/<int:pk>/', EmailMassageDetailView.as_view(), name='email_message_detail'),
]