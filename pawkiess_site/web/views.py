from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def owner_features(request):
    return render(request, 'owner_features.html')


def sitter_features(request):
    return render(request, 'sitter_features.html')


def pricing(request):
    return render(request, 'pricing.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    context = {"submitted": False}
    if request.method == 'POST':
        context["submitted"] = True
        context["name"] = request.POST.get('name', '')
    return render(request, 'contact.html', context)


def login_view(request):
    context = {"authenticated": False, "error": None}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Demo-only: mark as authenticated when fields present
        if email and password:
            context["authenticated"] = True
        else:
            context["error"] = "Please enter email and password."
    return render(request, 'login.html', context)


def signup(request):
    context = {"created": False, "error": None}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name and email and password:
            context["created"] = True
        else:
            context["error"] = "Please fill all required fields."
    return render(request, 'signup.html', context)
