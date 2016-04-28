from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.
from django.template import RequestContext
from Rebbit.models import Post, Person, Sub_rebb, Voting, Comment, CommentVoting



def homepage(request):
    subs = Sub_rebb.objects.order_by('sub_r')
    request.session['voted'] = "False"
    return render_to_response("Rebbit/homepage.html", {
        'Post_list': Post.objects.all(),
        'Subrebb_list': subs,
    }, context_instance=RequestContext(request))

def createpost(request):
    subs = Sub_rebb.objects.order_by('sub_r')
    c = {
        'Subrebb_list': subs,
    }
    c.update(csrf(request))
    return render_to_response("Rebbit/createpost.html",c,context_instance=RequestContext(request))

def auth_post(request):
    post = Post()
    post.title = request.POST.get('posttitle')
    web_user = Person.objects.get(username=request.session['user_username'])
    post.creator = web_user
    post.rpost = request.POST.get('postdescription')

    post.firstlink = request.POST.get('firstlink')

    post.secondlink = request.POST.get('secondlink')

    post.thirdlink = request.POST.get('thirdlink')
    try:
        postsubr = Sub_rebb.objects.get(sub_r=request.POST['topic'].lower())
        post.subreddit = postsubr
        post.save()
    except Sub_rebb.DoesNotExist:
        return render_to_response("Rebbit/createpost.html", {
            'invalid': True
        }, context_instance=RequestContext(request))

    return redirect("/index")

def auth_comment(request,sub_id,post_id):
    commentpost = Comment()
    commentpost.comment = request.POST.get('comment')
    web_user = Person.objects.get(username=request.session['user_username'])
    commentpost.creator = web_user
    name = Post.objects.get(id=post_id)
    commentpost.post = name
    commentpost.save()
    url = "http://127.0.0.1:8000/r/" + str(sub_id) + "/" + str(post_id)
    return HttpResponseRedirect(url)

def auth_verify(request):

    try:
        user = Person.objects.get(username=request.POST['username'])
         # the password verified for the user
        if user.password == request.POST['password']:
            request.session['user_fname'] = user.first_name
            request.session['user_lname'] = user.last_name
            request.session['user_email'] = user.email
            request.session['user_username'] = user.username
            return redirect("/account")
        else:
            return render_to_response("Rebbit/signin.html", {
            'invalid': True
            }, context_instance=RequestContext(request))
    except Person.DoesNotExist:
        user = None
        # the authentication system was unable to verify the username and password
        return render_to_response("Rebbit/signin.html", {
            'bothinvalid': True
        }, context_instance=RequestContext(request))

def subredditdetail(request,sub_id,post_id):
    post_info = Post.objects.get(id=post_id)
    comment_info = Comment.objects.filter(post=post_info)
    comment_info = comment_info.order_by('-count')
    num = 0
    if post_info.firstlink == "":
        num = num+1
    if post_info.secondlink == "":
        num = num+1
    if post_info.thirdlink == "":
        num = num+1

    if num == 3:
        c = {
            'Post_list': post_info,
            'invalid': True ,
            'comment_list': comment_info,
        }
        c.update(csrf(request))
        return render_to_response("Rebbit/subredditdetail.html", c, context_instance=RequestContext(request))

    else:
        c = {
            'Post_list': post_info,
            'comment_list': comment_info,
        }
        c.update(csrf(request))
        return render_to_response("Rebbit/subredditdetail.html", c, context_instance=RequestContext(request))


def votecomment(request,sub_id,post_id,comment_id):
    comid = comment_id
    comment_info = Comment.objects.get(id=comid)
    user = Person.objects.get(username=request.session['user_username'])
    try:
        vote = CommentVoting.objects.get(creator=user,votechoice=comment_info)
        context={

        }
        url = "http://127.0.0.1:8000/r/" + str(sub_id) + "/" + str(post_id)
        return HttpResponseRedirect(url)
    except CommentVoting.DoesNotExist:
        vote = CommentVoting()
        request.session['cvoted'] = "False"
        comment_info.count = comment_info.count + 1
        vote.creator = user
        vote.votechoice = comment_info
        vote.save()
        comment_info.save()
        url = "http://127.0.0.1:8000/r/" + str(sub_id) + "/" + str(post_id)
        return HttpResponseRedirect(url)

#voting: tied to post and person = person currently in session since cant vote unless logged
#first do try and catch, if vote exist say session variable=True and check that in html page
#create instance of vote, raise the vote by one and then save
def votepost(request,sub_id,post_id):
    sub = Sub_rebb.objects.get(sub_r=sub_id)
    post_info = Post.objects.get(id=post_id)
    user = Person.objects.get(username=request.session['user_username'])
    try:
        vote = Voting.objects.get(creator=user,votechoice=post_info)
        request.session['voted'] = "True"
        url = "http://127.0.0.1:8000/r/" + str(sub.sub_r) + "/" + str(post_info.id)
        return HttpResponseRedirect(url)
    except Voting.DoesNotExist:
        vote = Voting()
        request.session['voted'] = "False"
        post_info.count = post_info.count + 1
        vote.creator = user
        vote.votechoice = post_info
        vote.save()
        post_info.save()
        url = "http://127.0.0.1:8000/r/" + str(sub.sub_r) + "/" + str(post_info.id)
        return HttpResponseRedirect(url)

def subreddit(request,sub_id):
    sub = Sub_rebb.objects.get(sub_r=sub_id)
    sub_info = Post.objects.filter(subreddit=sub)
    return render_to_response("Rebbit/subreddit.html", {
        'subname': sub,
        'sub_list': sub_info,
        'reg_sub_list': Sub_rebb.objects.all(),
    }, context_instance=RequestContext(request))

def signup(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("Rebbit/signup.html",c)

def auth_signup(request):
    person = Person()
    person.first_name = request.POST.get('firstname')
    person.last_name = request.POST.get('lastname')
    person.email = request.POST.get('email')
    person.username = request.POST.get('username')
    person.password = request.POST.get('password')
    person.save()
    return redirect("/signin")

def signin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("Rebbit/signin.html",c)

def accounthome(request):

    return render_to_response("Rebbit/userhome.html", {
        'Person_list': Person.objects.all()
    }, context_instance=RequestContext(request))


def logout(request):
    if request.session.get('user_username', None):
        request.session.flush()
        return redirect("/index")
    else:
        return render_to_response("Rebbit/signin.html", {
            'notlogged': True
            }, context_instance=RequestContext(request))


def createsub(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("Rebbit/createsub.html",c,context_instance=RequestContext(request))

def auth_sub(request):
    sub = Sub_rebb()
    try:
        postsubr = Sub_rebb.objects.get(sub_r=request.POST['subname'])
        return render_to_response("Rebbit/createsub.html", {
            'invalid': True
        }, context_instance=RequestContext(request))
    except Sub_rebb.DoesNotExist:
        sub.sub_r = request.POST.get('subname').lower()
        sub.save()
        return redirect("/createpost")

def aboutus(request):
    return render_to_response("Rebbit/about.html", {
            }, context_instance=RequestContext(request))


