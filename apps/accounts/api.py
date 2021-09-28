from ninja import Router
from .tasks import fetch_daily_sales, sync_daily_sales_file_to_db
router = Router()


@router.get("/accounts/dailysales")
async def accounts(request):
    records = fetch_daily_sales()

    return records
