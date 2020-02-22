from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def create_user(request):
    return render(request, 'create-user.html')


def customer_portal(request):
    return render(request, 'customer-portal.html')


def admin_portal(request):
    return render(request, 'admin-portal.html')


def make_donation(request):
    return render(request, 'make-donation.html')


def book_event(request):
    return render(request, 'book-event.html')


def class_signup(request):
    return render(request, 'class-signup.html')


def volunteer(request):
    return render(request, 'volunteer.html')


def request_homecare(request):
    return render(request, 'request-homecare.html')


def request_shuttle(request):
    return render(request, 'request-shuttle.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def view_events(request):
    return render(request, 'view-events.html')


def view_equipment(request):
    return render(request, 'view-equipment.html')


def view_classes(request):
    return render(request, 'view-classes.html')