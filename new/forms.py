from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Patients, User,Doctor
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('patients', 'Patients'), ('doctor', 'Doctor')], widget=forms.RadioSelect)
    
class PatientsSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False) 
    address_line1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'password1', 'password2')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_patients = True
        user.save()
        patients = Patients.objects.create(user=user)
        patients.profile_picture=self.cleaned_data.get('profile_picture')
        patients.address_line1=self.cleaned_data.get('address_line1')
        patients.city=self.cleaned_data.get('city')
        patients.state=self.cleaned_data.get('state')
        patients.pincode=self.cleaned_data.get('pincode')
        patients.save()
        return patients


class DoctorSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False) 
    address_line1 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.profile_picture=self.cleaned_data.get('profile_picture')
        doctor.address_line1=self.cleaned_data.get('address_line1')
        doctor.city=self.cleaned_data.get('city')
        doctor.state=self.cleaned_data.get('state')
        doctor.pincode=self.cleaned_data.get('pincode')
        doctor.save()

        return doctor



