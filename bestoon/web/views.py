from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense
from datetime import datetime

# Create your views here.

@csrf_exempt
def submit_expense(request):
    """user submits an expense"""

    # TODO; validate data. user might be fake. token might be fake, amount might be...
    this_token = request.POST.get('token', None)
    if this_token:
        this_user = User.objects.filter(token__token=this_token).first()
        if this_user:
            if 'date' not in request.POST.get:
                date = datetime.now()
            Expense.objects.create(
                user=this_user,
                amount=request.POST.get('amount', None),
                text=request.POST.get('text', None),
                date=date
            )
            return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': 'ok'}, status=400)
    else:
        return JsonResponse({'status': 'ok'}, status=400)
