from django.shortcuts import render,redirect
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


def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        # photo = request.POST['photo']
        print(name, email, phone, address)
        contact = Contact(name= name,email=email,phone_number=phone,
                          address=address, user = request.user)
        contact.save()
        return redirect('contact')
    return render(request, 'add.html')

    
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     message = request.POST['message']
    #     contact = Contact(name=name,email=email,phone=phone,message=message,user=request.user)
    #     contact.save()
    #     return redirect('contact')
    # else:
    #     return render(request, 'add_contact.html')
