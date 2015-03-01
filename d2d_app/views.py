from django.shortcuts import render
from d2d_app.models import Customer, Contract, Package
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated():
        current_user = Customer.objects.get(user=request.user)
        # Find all contracts set up by current user   
        selling = Contract.objects.filter(seller=current_user)
        buying = Contract.objects.filter(buyer=current_user)
        context = {
            'selling': selling,
            'buying': buying,
        }
        return render(request, 'd2d_app/index.html', context) 
    else:
        return render(request, 'd2d_app/index.html')

def register_view(request):
    return render(request, 'd2d_app/register.html')

def register_post(request):
    username = request.POST['username']
    password = request.POST['password']
    User.objects.create_user(username=username, password=password) 
    user = authenticate(username=username, password=password)
    Customer.objects.create(user=user)
    login(request, user)
    return index(request)

def login_view(request):
    return render(request, 'd2d_app/login.html')

def check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
    else:
        pass
    return index(request) 

def logout_view(request):
    logout(request)
    return index(request)

def pay(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    contract.payed = True
    contract.save()
    return index(request)

def satisfied(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    # For now deleting items when buyer is satisfied
    contract.package.delete()
    contract.delete()
    return index(request)

def add_contract_view(request):
    """ If post contains a new entry, this is added to database, otherwise a new one can be added """
    # TODO Add checks for valid data, learn how to nicely style the generic views
    new_contract = request.POST
    add_error = False
    if len(new_contract) == 0:
        added_contract = False
    else:
        # An add request was sent
        added_contract = True
        buyer = User.objects.get(username=request.POST.get('buyer', None)) #TODO No checks for valid user at the moment!
        buyer_customer = Customer.objects.get(user=buyer)
        weight = request.POST.get('weight', None)
        height = request.POST.get('height', None)
        width = request.POST.get('width', None)
        length = request.POST.get('length', None)
        price = request.POST.get('price', None)
        description = request.POST.get('description', None)
        seller = Customer.objects.get(user=request.user)

        # New package
        package = Package.objects.create(description=description, price=price, height=height, length=length, width=width, weight=weight) 

        # New contract
        Contract.objects.create(seller=seller, package=package, buyer=buyer_customer)

    context = { 'added_success': added_contract }
    return render(request, 'd2d_app/add_contract.html', context)

def remove(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    contract.package.delete()
    contract.delete()
    
    return index(request)
