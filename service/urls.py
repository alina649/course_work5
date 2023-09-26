from django.urls import path
from . import views
from service.apps import ServiceConfig
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    MailingListView, \
    MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    MailingManagerUpdateView

app_name = ServiceConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),


    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailingView/<int:pk>/', MailingDetailView.as_view(), name='mailing_view'),
    path('mailingEdit/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
    path('mailingDelete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),

    path('manager_edit_mailing/<int:pk>', MailingManagerUpdateView.as_view(), name='manager_mailing_update'),
]