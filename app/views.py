from django.shortcuts import render, redirect, get_object_or_404
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
            return render(request, 'contact_form.html', {'form':form})
    else:
        form = ContactsForm()
        return render(request, 'contact_form.html', {'form':form})

# def about_contact(request, c_id):
#     contact = Contact.objects.get(id=c_id)
#     return render(request, 'about_contact.html', {'contact':contact})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactsForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactsForm(instance=contact)

# Create your views here.
