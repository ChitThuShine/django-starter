from ninja import NinjaAPI
from apps.accounts.api import router as accounts_router
api = NinjaAPI()


api.add_router("/accounts/", accounts_router)