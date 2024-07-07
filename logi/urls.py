from django.urls import path

from logi.views import LogiListView

app_name = 'logi'

urlpatterns = [
    path('logs_list/', LogiListView.as_view(), name='logs_list'),
]
