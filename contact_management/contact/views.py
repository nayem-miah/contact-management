from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact,UserNote
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def contact(request):
    template = 'contact.html'
    user = request.user
    checkdata = Contact.objects.filter(user=user)
    context = {
        'check': checkdata
    }

    return render(request,context=context,template_name = template)



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
