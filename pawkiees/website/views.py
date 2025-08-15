from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html', {"page_title": "Home"})


def services(request):
    return render(request, 'website/services.html', {"page_title": "Services"})


def sitters(request):
    return render(request, 'website/sitters.html', {"page_title": "Sitters"})


def booking(request):
    return render(request, 'website/booking.html', {"page_title": "Booking"})


def about(request):
    return render(request, 'website/about.html', {"page_title": "About"})


def contact(request):
    return render(request, 'website/contact.html', {"page_title": "Contact"})
