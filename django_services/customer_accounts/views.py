from django.shortcuts import render
from .models import Customer

def account_info(request):
    customer = Customer.objects.first()  # Retrieve customer data, adjust as needed
    return render(request, 'customer_accounts/account_info.html', {'customer': customer})
