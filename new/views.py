from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView

from .forms import PatientsSignUpForm,DoctorSignUpForm
from .models import User, Patients, Doctor

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def SignUp(request):
	return render(request,'main.html')


class PatientsSignUpView(CreateView):
    model = Patients
    form_class = PatientsSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patients'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        
        return redirect('main')


class DoctorSignUpView(CreateView):
    model = Doctor
    form_class = DoctorSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('main')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            return redirect('dashboard')
            
    else:
        form = AuthenticationForm()
    return render(request, 'main.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
     
    if user.is_patient:
        patients = Patients.objects.filter(user=user)
        
        return render(request, 'patient_dashboard.html', {'user': user, 'patients': patients})
     
    elif user.is_doctor:
        doctor =  Doctor.objects.filter(user=user) 
        
        return render(request, 'doctor_dashboard.html', {'user': user, 'doctor': doctor})  
    else:
        # Handle other user types or error
        pass

