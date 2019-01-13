"""Imported functions, packages, methods as per requirements"""
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime

from . models import Profile, Post
from . forms import Blog_Feed_Back

""" index_login_signup function renders the index page and checks which submit (Login/Signup) is clicked if login clicked it calls login
    functon or it calls register function, """
def index_login_signup(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('signup-button') == 'signUpTo':
            return registration(request)

        elif request.POST.get('login-button') == 'loginTo':
            return user_login(request)

        elif request.POST.get('search_box'):
            # call search functon
            pass
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login_function'))
        else:
            context['form'] = UserCreationForm()
            return render(request, 'MYBLOG/index.html', context)



"""The signup() functon checks whether the method is post or not if yes it checks for the value is signup if yes it calls
the register function or it calls the login function"""
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('login_function'))
    else:
        form = UserCreationForm()
    return render(request, 'MYBLOG/profile.html', {'form': form})


"""Declaration of login function which is called in signup function if the value of submit button is not 'signup_to then'"""
def user_login(request):
    context = {}
    username = request.POST['username']
    password = request.POST['password']
    user     = authenticate(request, username = username, password = password)
    if user:
        login(request, user)
        user_session = request.session['username'] = request.POST.get('username')
        return HttpResponseRedirect(reverse('login_function'))
    else:
        context['error'] = 'Incorrect Credentials!'
        return render(request, 'MYBLOG/index.html', context)



"""welcome_home function does nothing but displays data to the home and works as an UI for the users"""
@login_required(login_url = '/')
def welcome_home(request):
    context = {}
    context['user']= request.user
    blogs = display_blog(request)
    context.update(blogs)
    return render(request, 'MYBLOG/home.html', context)


"""Visit_again() function just logs out from the system and redirects to the index page where an  user ca login again"""
def visit_again(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('index_login_signup_function'))

"""post a blog function is used to post an article to the database"""
def post_blog(request):
    context = {}
    active_user = request.user
    if request.method == 'POST':
        title           = request.POST.get('titleofArticle')
        about           = request.POST.get('aboutArticle')
        article         = request.POST.get('articleContent')
        author          = Profile.objects.get(username = active_user)
        publish_time    = datetime.now()

        publish         = Post(title = title, about = about, article = article, author = author, publish_date = publish_time)
        publish.save()
        context['message'] = 'Your Articles has been published'
        return render(request, 'MYBLOG/post.html', context)
    else:
        return render(request, 'MYBLOG/post.html', context)

"""View Profile Section and edit profile section ----------------------------------------------------------------------------------------"""
"""This function is under construction make sure you don't mess up things"""
def view_profile(request):
    context = {}
    logged_in_user = request.user

    user_row = User.objects.get(username = logged_in_user)
    full_name = user_row.first_name + ' ' + user_row.last_name
    profile_row = Profile.objects.get(username = user_row.id)

    if request.method == 'POST':
        fname       = request.POST.get('first_name')
        lname       = request.POST.get('last_name')
        profession  = request.POST.get('Profession')
        mobile      = request.POST.get('mobile')
        email       = request.POST.get('email')
        location    = request.POST.get('location')
        user_row.first_name = fname
        user_row.last_name = lname
        user_row.profile.profession = profession
        user_row.profile.mobile = mobile
        user_row.profile.location = location
        user_row.save()

        print(fname, lname,profession,mobile,email,location)
    context = {
        'user': user_row,
        'full_name': full_name,
        'profile_img':profile_row.profile_img,
        'website': profile_row.website,
        'first_name': user_row.first_name,
        'job': user_row.profile.profession
    }
    print(context['job'])
    return render(request, 'MYBLOG/profile.html', context)


"""The function called display blog return blogs to the welcome home function where all the blogs posted by authors will be published """
def display_blog(request):
    context = {}
    all_blogs = Post.objects.all().order_by('-publish_date')
    return {'post_row': all_blogs}

# The below functon expend_post works on clicking view details link on each post and enlarges the post into full form. where
# a reader can read the entire article and comment his views and share with friends and family
def expand_post(request, post_id):
    this_post = Post.objects.get(id = post_id)
    form = Blog_Feed_Back()
    author = User.objects.get(username = this_post.author)
    authors_full_name = author.first_name+ ' ' + author.last_name

    context = {'post': this_post.article, 'title': this_post.title, 'published_on': this_post.publish_date, 'form': form, 'author': authors_full_name}
    return render(request, 'MYBLOG/expanded_post.html', context)
