from django.urls import path

from message.views import MessageListView, MessageCreateView, MessageDeleteView, MessageUpdateView, MessageDetailView

app_name = 'message'

urlpatterns = [
    path('', MessageListView.as_view(), name='message'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
