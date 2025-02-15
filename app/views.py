from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactsForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactsForm()
        return render(request, 'contact_form.html')

# Create your views here.
