from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact,UserNote
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def contact(request):
    if request.user.is_authenticated:
        template = 'contact.html'
        user = request.user
        checkdata = Contact.objects.filter(user=user)
        context = {
            'check': checkdata

        }
        return render(request,context=context,template_name = template)
    else:
        return redirect('login')
      
      
def _login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, log the user in
            login(request, user)
            return redirect('contact')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
           
    return render(request, 'login.html')
def sign_up(request):
   if request.user.is_authenticated:
    return redirect('contact') 
   else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password = password)
        user.save()
        return redirect('login')
    return render(request,'sign_up.html')
   
def log_out(request):
    logout(request)
    return redirect('login')
@login_required
def user_notes(request):
    user = request.user
    notes = UserNote.objects.filter(user=user)
    return render(request, 'notes.html', {'notes': notes})

@login_required
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        print(name, email, phone, address)
        contact = Contact(name= name,email=email,phone_number=phone,
                          address=address, user = request.user)
        contact.save()
        return redirect('contact')
    return render(request, 'add.html')

@login_required
def edit_contact(request,pk=None):
     item = get_object_or_404(Contact, id=pk)

     if request.method == 'POST':
         name = request.POST['name']
         email = request.POST['email']
         phone = request.POST['phone']
         address = request.POST['address']
        
         item.name = name
         item.email = email
         item.phone_number = phone
         item.address = address
         item.save()
         return redirect('contact')
         
     return render(request, 'edit_contact.html', {'item': item})


@login_required
def delete_contact(request,pk=None):
    item = get_object_or_404(Contact, id=pk)
    item.delete()
    return redirect('contact')

def search_contacts(request):
    
    searched = request.GET['searched']
    searched_contact = Contact.objects.filter(name__contains = searched)
    return render(request,'search.html', {'searched':searched_contact})