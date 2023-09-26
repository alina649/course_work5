from django.contrib import admin

from service.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'stop_time', 'frequency', 'status', 'owner', '_clients')
    list_filter = ('status',)

    def _clients(self, row):
        return ','.join([x.email for x in row.clients.all()])

