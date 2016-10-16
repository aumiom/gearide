import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from bike.authentication import create_user, login_view


def index_page(request):
    message = ""
    print "request ajax:::::::::::::::::::" + str(request.is_ajax())
    print "request body:::::::::::::::::::" + request.body
    print "request method:::::::::::::::::" + request.method
    if request.method == 'POST':
        if request.is_ajax() and "firstname" in request.body:
            #Signup
            print ":::::::::::::::::::::::SIGN UP::::::::::::::::::::::::::::"
            json_val = json.loads(request.body)
            template = loader.get_template('index.html')
            signup_message = create_user(json_val['firstname'], json_val['lastname'], json_val['email'], json_val['password'])
            login_message = login_view(request, json_val['email'],json_val['password'])
            print signup_message
            print login_message
            return HttpResponse(template.render({'message': message}, request))
        elif request.is_ajax():
            #Login
            print ":::::::::::::::::::::::::::LOGIN:::::::::::::::::::::::::::"
            json_val = json.loads(request.body)
            template = loader.get_template('index.html')
            message = login_view(request, json_val['email'],json_val['password'])
            print message
            return HttpResponse(template.render({'message': message}, request))
        else:
            #CSRF Token
            print ":::::::::::::::::::::::::::CSRF::::::::::::::::::::::::::::"
            return render(request, 'index.html', {'message': message})
    else:
        #Normal request
        print ":::::::::::::::::::::::::::NORMAL:::::::::::::::::::::::::::::::"
        return render(request, 'index.html', {'message': message})


def search_page(request):
    message = ""
    print "request ajax:::::::::::::::::::" + str(request.is_ajax())
    print "request body:::::::::::::::::::" + request.body
    print "request method:::::::::::::::::" + request.method
    if request.method == 'POST':
        if request.is_ajax():
            json_val = json.loads(request.body)
            template = loader.get_template('search.html')
            create_user(json_val['firstname'], json_val['lastname'], json_val['email'], json_val['password'])
            message = "You have successfully logged in"
            return HttpResponse(template.render({'message': message}, request))
        else:
            return render(request, 'search.html', {'message': message})
    else:
        return render(request, 'search.html', {'message': message})


@login_required()
def checkout_page(request):
    print request.user
    return render_to_response('checkout.html')
