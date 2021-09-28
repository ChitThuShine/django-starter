from django.shortcuts import render
from django.views.generic import TemplateView

from .tasks import sync_daily_sales_file_to_db
class AccountsView(TemplateView):

    template_name = "accounts/base_accounts.html"
    def get_context_data(self, **kwargs):
        sync_daily_sales_file_to_db()
        context = super().get_context_data(**kwargs)
        return context
    