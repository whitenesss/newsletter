from django.urls import path
from django.views.decorators.cache import cache_page
from clients.views import ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView, HomeView, \
    ClientDetailView

app_name = 'clients'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('clients', ClientListView.as_view(), name='clients_list'),
    path('client_create', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', cache_page(60)(ClientDetailView.as_view()), name='client_detail'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),

]
