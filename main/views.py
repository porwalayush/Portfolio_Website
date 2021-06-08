from django.shortcuts import render,redirect
from .models import New_Message
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def connect(request):
	if request.method== 'POST':
		name=request.POST['name']
		email=request.POST['email']
		sbject=request.POST['subject']
		mssage=request.POST['message']
		new_message=New_Message.objects.create(Name=name,Email=email,Subject=sbject,Message=mssage)
		new_message.save()
		subject = 'New Connection'
		message = 'ThankYou for connecting with me(Ayush Porwal), I will reach out to you soon.'
		recepient = email
		send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently=False)

		subject1='ATTENTION, '+name+' '+'SEND A MESSAGE ON PORTFOLIO SITE'
		message1='subject:'+sbject+' & message:'+mssage
		recepient1 = 'ayushporwal3843@gmail.com'
		send_mail(subject1,message1, EMAIL_HOST_USER, [recepient1], fail_silently=False)
		messages.success(request, 'Message Send Successfully.')
		return redirect('main')
	else:
		return redirect('main')


