from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages

from .models import Contact
from .forms import NewContactForm


def contact_search(request):
    query = request.GET

    if query:
        first_name = query.get('first_name')
        last_name = query.get('last_name')
        phone_number = query.get('phone_number')
        email_address = query.get('email_address')
        contacts = Contact.objects.filter(
            first_name__icontains=first_name,
            last_name__icontains=last_name,
            phone_number__icontains=phone_number,
            email_address__icontains=email_address
            ).order_by('created_date')
    else:
         contacts = Contact.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'cmlite/contact_search.html', {'contacts' : contacts})


def add_contacts(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        new_contact = NewContactForm(request.POST)
        if new_contact.is_valid():
            contact = new_contact.save(commit=False)
            contact.owner = request.user
            contact.created_date = timezone.now()
            contact.save()
            messages.add_message(request, messages.INFO, 'You just added ' + first_name + ' ' + last_name + ' to your contacts!')
    else:
        new_contact = NewContactForm()
    return render(request, 'cmlite/add_contacts.html', {'new_contact': new_contact})

def quick_search(request):
    if request.method== 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']
    else:
        first_name = ''
        last_name = ''
        phone_number = ''
        email_address = ''
    contacts = Contact.objects.filter(
    first_name__icontains=first_name,
    last_name__icontains=last_name,
    phone_number__icontains=phone_number,
    email_address__icontains=email_address
    ).order_by('created_date')
    return render(request, 'cmlite/quick_search.html', {'contacts' : contacts})
