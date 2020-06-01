from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')    

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointment = Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctors:
        d+=1  
    for i in patients:
        p+=1  
    for i in appointment:
        a+=1          
    d1={'d':d,'p':p,'a':a}    
    return render(request,'index.html',d1)    



def login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"    
        except:
            error="yes"        
    d = {'error':error}   
    return render(request,'login.html',d)      


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')     


def view_doctor(request):
     if not request.user.is_staff:
        return redirect('login')
     doc = Doctor.objects.all() 
     d = {'doc':doc}  
     return render(request,'view_doctor.html',d)   


def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['contact']
        c = request.POST['special']
        
        try:
            Doctor.objects.create(name=a,mobile=b,special=c)
            error="no"
              
        except:
            error="yes"        
    d = {'error':error}   
    return render(request,'add_doctor.html',d)           

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def view_patient(request):
     if not request.user.is_staff:
        return redirect('login')
     pat = Patient.objects.all() 
     d = {'pat':pat}  
     return render(request,'view_patient.html',d)   


def add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['gender']
        c = request.POST['mobile']
        d = request.POST['address']
        
        try:
            Patient.objects.create(name=a,gender=b,mobile=c,address=d)
            error="no"
              
        except:
            error="yes"        
    d = {'error':error}   
    return render(request,'add_patient.html',d)           

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def view_appointment(request):
     if not request.user.is_staff:
        return redirect('login')
     appoint = Appointment.objects.all() 
     d = {'appoint':appoint}  
     return render(request,'view_appointment.html',d)   


def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        a = request.POST['doctor']
        b = request.POST['patient']
        c = request.POST['date']
        d = request.POST['time']
        doctor = Doctor.objects.filter(name=a).first()
        patient = Patient.objects.filter(name=b).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=c,time1=d)
            error="no"
              
        except:
            error="yes"        
    d = {'doctor':doctor1,'patient':patient1,'error':error}   
    return render(request,'add_appointment.html',d)           

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')

    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')    