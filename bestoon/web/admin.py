from django.contrib import admin
from .models import Expense, Token
# Register your models here.

admin.site.register(Expense)
admin.site.register(Token)