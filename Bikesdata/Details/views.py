from django.shortcuts import render,redirect
from django.http import HttpResponse
from Details.forms import Usregis,Upd,Pad,OrderForm
from Bikesdata import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Details.models import Exfd,YourOrder

# Create your views here.

def home(request):
	return render(request,'sd/home.html')

def about(request):
	return render(request,'sd/about.html')

@login_required
def contact(request):
	return render(request,'sd/contact.html')

def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			sb = "Testing Email to register for Bikesdata project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or user name or password")
			# print(p.username,p.email)
	y =Usregis()
	return render(request,'sd/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'sd/dashboard.html')

@login_required
def prfle(request):
	return render(request,'sd/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd)
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'sd/updateprofile.html',{'r':p,'q':t})

@login_required
def vds(request):
	return render(request,'sd/viewsDetails1.html')

@login_required
def ordls(request):
	p = YourOrder.objects.filter(m_id=request.user.id)
	return render(request,'sd/Order.html',{'y':p})

@login_required
def corlist(request):
	if request.method == "POST":
		r = OrderForm(request.POST)
		if r.is_valid():
			t = r.save(commit=False)
			t.m_id = request.user.id
			t.save()
			messages.success(request,"successfully Booked Please contact our employee for further Details ")
			return redirect('/ord')
	r = OrderForm()
	return render(request,'sd/list.html',{'d':r})

@login_required
def vdds(request):
	return render(request,'sd/viewsDetails2.html')

@login_required
def vi(request):
	return render(request,'sd/viewsDetails3.html')

@login_required
def lik(request):
	return render(request,'sd/viewsDetails4.html')

@login_required
def su(request):
	return render(request,'sd/viewsDetails5.html')

@login_required
def sd(request):
	return render(request,'sd/viewsDetails6.html')

@login_required
def companies(request):
	return render(request,'sd/company.html')