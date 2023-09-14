from django.urls import path
from . import views
from service.apps import ServiceConfig
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    MessageListView, MessageCreateView, MessageDetailView, MessageDeleteView, MessageUpdateView, MailingListView, \
    MailingCreateView, MailingDetailView

app_name = ServiceConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('messagesView/<int:pk>/', MessageDetailView.as_view(), name='view'),
    path('messagesDelete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('messagesEdit/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),

    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailingView/<int:pk>/', MailingDetailView.as_view(), name='mailing_view')
]