from django.test import TestCase
from .models import Contact
from django.utils import timezone
from .forms import NewContactForm
from django.urls import reverse
# Create your tests here.

class ContactTest(TestCase):

    def create_contact(self, first_name="John", last_name="Doe", phone_number="1234567890", email_address="john.doe@gmail.com"):
        return Contact.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, email_address=email_address, created_date=timezone.now(), owner_id=3)

    def test_contact_creation(self):
        c = self.create_contact()
        self.assertTrue(isinstance(c, Contact))
        self.assertEqual(c.first_name, "John")
        self.assertEqual(c.last_name, "Doe")
        self.assertEqual(c.phone_number, "1234567890")
        self.assertEqual(c.email_address, "john.doe@gmail.com")


    def test_contact_search_view(self):
        c = self.create_contact()
        url = reverse("contact_search")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(str.encode(c.email_address), resp.content)

    def test_valid_form(self):
        c = Contact.objects.create(first_name="Jane", last_name="Doe", phone_number="1234567890", email_address="123@test.com", created_date=timezone.now(), owner_id=3)
        data = {'first_name': c.first_name, 'last_name': c.last_name, 'phone_number': c.phone_number, 'email_address': c.email_address, 'created_date': c.created_date, 'owner_id': c.owner_id}
        form = NewContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_email_form(self):
        c = Contact.objects.create(first_name="Juniper", last_name="Doe", phone_number="1234567890", email_address="NOTANEMAIL", created_date=timezone.now(), owner_id=3)
        data = {'first_name': c.first_name, 'last_name': c.last_name, 'phone_number': c.phone_number, 'email_address': c.email_address, 'created_date': c.created_date, 'owner_id': c.owner_id}
        form = NewContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_phone_form(self):
        c = Contact.objects.create(first_name="Joey", last_name="Doe", phone_number="NOTAPHONENUMBER", email_address="joey.doe@gmail.com", created_date=timezone.now(), owner_id=3)
        data = {'first_name': c.first_name, 'last_name': c.last_name, 'phone_number': c.phone_number, 'email_address': c.email_address, 'created_date': c.created_date, 'owner_id': c.owner_id}
        form = NewContactForm(data=data)
        self.assertFalse(form.is_valid())
