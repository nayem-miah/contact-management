from django.shortcuts import render
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
    print('this is note.......',notes)
    return render(request, 'notes.html', {'notes': notes})