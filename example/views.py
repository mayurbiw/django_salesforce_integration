from django.shortcuts import render, HttpResponse
from . models import Account, Product, User, CoreAccount

# Create your views here.

def index(request):
    return render(request,'index.html',{})


def list_accounts(request):
    accounts = Account.objects.all()

    return render(request, 'list-accounts.html',
                            dict(title="List First 5 Accounts", accounts=accounts)
                            )

def add_account(request):
    
    if request.method == "GET":
        users = User.objects.all()
        usernames = [u.Username for u in users]
        return render(request,'add_account.html',dict(title ="All the possible owners",usernames=usernames))
    
    if request.method == "POST":
        name = request.POST['Name']
        owner = request.POST['Owner'] 
        type = Type = request.POST['type']
        billing_street = request.POST['BillingStreet']
        billing_city = request.POST['BillingCity']
        billing_state = request.POST['BillingState']
        billing_postal_code =  request.POST['BillingPostalCode']
        billing_country =  request.POST['BillingCountry']
        shipping_street =  request.POST['ShippingStreet']
        shipping_city = request.POST['ShippingCity']
        shipping_state = request.POST['ShippingState']
        shipping_postal_code =request.POST['ShippingPostalCode']
        shipping_country = request.POST['ShippingCountry']
        website = request.POST['Website']
        phone = request.POST['Phone']
        industry = request.POST['Industry']
        description = request.POST['Desciption']
        
        #get the user of the owner 
        try:
            user = User.objects.get(Username=owner)
        except Exception:
            return HttpResponse("The owner does not exists in the system")

        account = Account(Owner = user, 
                            Name = name,Type=type,BillingStreet=billing_street,BillingCity=billing_city,
                            BillingState = billing_state, BillingPostalCode=billing_postal_code,
                            BillingCountry = billing_country, ShippingStreet = shipping_street,ShippingCity=shipping_city,
                            ShippingState = shipping_state,ShippingPostalCode = shipping_postal_code,ShippingCountry=shipping_country,
                            Phone = phone,Website=website, Industry=industry,Description  = description)
            
        account.save()
        return HttpResponse("The new account is created..")

    
