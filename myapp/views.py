from django.shortcuts import render
from .models import Users, Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')



def trainer(request):
    return render(request, 'trainer.html')


def why(request):
    return render(request, 'why.html')


def blog(request):
    return render(request, 'blog.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # create an object
        new_person = Users(first_name=first_name, last_name=last_name, email=email, password=password)
        new_person.save()

        # get all persons-displays everything in the database.
    people = Users.objects.all()
    return render(request, 'register.html', context={'people': people})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        # create an object
        savecontact = Contact(name=name, email=email, phone=phone, message=message)
        savecontact.save()
    return render(request, 'contact.html')
