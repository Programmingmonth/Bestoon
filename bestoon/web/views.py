from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense
# Create your views here.

@csrf_exempt

def submit_expense(request):
    """user submits an expense"""

    this_token = request.Post['token']
    this_user = User.objects.filter(token__token = this_user).get()
    Expense.objects.create(user = this_user, amount=request.POST['amount']
            text = request.POST['text'], date=now)
    print ("I'm in submit expense")
    print (request.POST)


    return JsonResponse({
        'status': 'ok' 
    }, encoder=JSONEncoder)
