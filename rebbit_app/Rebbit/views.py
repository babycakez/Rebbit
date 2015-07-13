from django.shortcuts import render_to_response, redirect, render
from django.core.context_processors import csrf
# Create your views here.
from django.template import RequestContext
from Rebbit.models import Post, Person, Sub_rebb


def homepage(request):

    return render_to_response("Rebbit/homepage.html", {
        'Rebbit': Post.objects.all()
    }, context_instance=RequestContext(request))

def subreddit(request):

    return render_to_response("Rebbit/subrebbit.html", {
        'Rebbit': Post.objects.all()
    })

def signup(request):

    return render_to_response("Rebbit/signup.html", {
        'Rebbit': Person.objects.all()
    })

def signin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("Rebbit/signin.html",c)

def accounthome(request):

    return render_to_response("Rebbit/userhome.html", {
        'Rebbit': Person.objects.all()
    }, context_instance=RequestContext(request))

def auth_verify(request):
    web_user = Person.objects.get(username=request.POST['username'])
    if web_user.password == request.POST['password']:
        request.session['user_fname'] = web_user.first_name
        request.session['user_lname'] = web_user.last_name
        request.session['user_email'] = web_user.email
        request.session['user_username'] = web_user.username
        return redirect("/account")
    else:
        return redirect("/signin")
def logout(request):
    del request.session['user_fname']
    del request.session['user_lname']
    del request.session['user_email']
    del request.session['user_username']
    return redirect("/index")