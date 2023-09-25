from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from service.forms import MailingForm
from service.models import Client, Message, Mailing, MailingLogs
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

"""Вид для Клиентов"""


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('service:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    """Контроллер блога для удаления карточки клиента"""

    model = Client
    success_url = reverse_lazy('service:client_list')


class ClientUpdateView(UpdateView):
    """Контроллер блога для изменения карточки клиента"""

    model = Client
    fields = ('full_name', 'email', 'comment')

    def get_success_url(self):
        """
        Переопределение url-адреса для перенаправления
        после успешного редактирования
        """

        return reverse('service:client_view', args=[self.object.pk])


"""Вид для Сообщений"""


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'body', 'is_active')
    success_url = reverse_lazy('service:message_list')


class MessageDeleteView(DeleteView):
    """Контроллер блога для удаления сообщения"""

    model = Message
    success_url = reverse_lazy('service:message_list')


class MessageUpdateView(UpdateView):
    """Контроллер блога для изменения карточки клиента"""

    model = Message
    fields = ('subject', 'body', 'is_active')

    def get_success_url(self):
        """
        Переопределение url-адреса для перенаправления
        после успешного редактирования
        """

        return reverse('service:view', args=[self.object.pk])


"""Вид для Рассылок"""


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                owner=user.pk
            )
        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('service:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    """Контроллер блога для изменения карточки клиента"""

    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        """
        Переопределение url-адреса для перенаправления
        после успешного редактирования
        """

        return reverse('service:mailing_view', args=[self.object.pk])


class MailingDeleteView(DeleteView):
    """Контроллер блога для удаления сообщения"""

    model = Mailing
    success_url = reverse_lazy('service:mailing_list')


class MailingLogsView(LoginRequiredMixin, ListView):
    model = MailingLogs
    template_name = 'mailsender/mailinglog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset