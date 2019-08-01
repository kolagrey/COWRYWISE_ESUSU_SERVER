from django.contrib import admin

# Register your models here.
from .models import Account, AccountGroup, GroupPayoutList, GroupContribution, GroupPayoutLog

admin.site.register(Account)
admin.site.register(AccountGroup)
admin.site.register(GroupPayoutList)
admin.site.register(GroupContribution)
admin.site.register(GroupPayoutLog)