from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def create_user(firstname, lastname, email, password):
    try:
        user = User.objects.get(email=email)
        message = "User %s already exist" % user.email
    except:
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        message = "User %s created successfully" %user.first_name
    return message


def change_password(email, password):
    try:
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        message = "Password for user %s changed successfully"
    except:
        message = "User %s does not exist in our user db" % (email)
    return message



def login_view(request, email, password):
    user = authenticate(username=email, password=password)
    print "User:::::::::::"+str(user)
    if user is not None:
        login(request, user)
        message = "User %s logged in successfully",email
    else:
        message = "User %s is not authorized to view this page",email
    return message



def logout_view(request):
    logout(request)

