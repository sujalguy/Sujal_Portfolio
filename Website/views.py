from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request,"Website/home.html")


def view_project(request):
    return render(request,"Website/project.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")

        full_message=f"Name:{name},\nEmail: {email},\n Message:{message}"

        send_mail(
            subject=f"Portfolio Enquiry from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["sujalgajbhiye10@gmail.com"]
        )
        messages.success(request,"Ypur message has been sent successfully")
        return render(request,"Website/email.html")

    return render(request,"Website/email.html")




