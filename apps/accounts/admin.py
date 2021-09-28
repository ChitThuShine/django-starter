from apps.accounts.tasks import fetch_daily_sales
from apps.accounts.models import DailyEntry
from django.contrib import admin
from .models import DailyEntry

# Register your models here.

@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ('product', 'date', 'sold')

    actions = ["add_entry_to_db"]

    def add_entry_to_db(self, request, queryset):
        records = fetch_daily_sales()
        for record in records:
            rec = { k.lower():v for k,v in record.items()}
            print(rec)
            obj, _ = DailyEntry.objects.get_or_create(**rec)

