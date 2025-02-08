from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.object.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


# Create your views here.
