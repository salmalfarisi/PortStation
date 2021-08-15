from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
import json

# import model
from .models import *

# import form
from .forms import *

# import library for registration, login and auth
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from uuid import uuid4

# import date
import datetime
# import var_dump library for python
from pprint import pprint
# import pagination
from django.core.paginator import Paginator
# import random data
import random
# make push notification
from notifications.signals import notify
# sorting data
import operator
from django.db import connection, transaction
# sending email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
# import filter manual
from django.db.models import Q


@login_required(login_url='login')
def Home(request):
	# login and user will redirect into this function 
	
def SignIn(request):
	# authenficate before user login into portstation

def Register(request):
	# register user data before using portstation

def Resetpassword(request, verificationtoken):
	# validate token link and reset user password

def Sendemail(request, subject, title, message, target):
	# send email via mailnest
	subject, from_email, to = subject, 'admin@portstation', target
	text_content = title
	html_content = message
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def Forgotpassword(request):
	# validate user email input and send token via email

def Signout(request):
	# log out user account including all active session

# CRUD for POST
@login_required(login_url='login')
def Createpost(request):
	# create and validate users post

@login_required(login_url='login')
def Editpost(request, id):
	# edit and validate users post

# see of detail post
@login_required(login_url='login')
def Showpost(request, id):
	# show all post data include all commentator
	
def Deletepost(request, id, currenturl):
	# Delete post by id

# CRUD for forum
def Indexforum(request):
	# show all forum data 

@login_required(login_url='login')
def Createforum(request):
	# create and validate user article before publish into public

def Showforum(request, id):
	# show article by id
	
@login_required(login_url='login')
def Editforum(request, id):
	# edit and validate user article before publish into public
	
@login_required(login_url='login')
def Deleteforum(request, id):
	# delete forum data

# cookie a.k.a session system
def Cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
	
def Cookie_delete(request):
	if request.session.test_cookie_worked():
		request.session.delete_test_cookie()
		response = HttpResponse("dataflair<br> cookie createed")
	else:
		response = HttpResponse("cookie telah dihapus")
	return response

def Create_session(request, data):
	account = User.objects.get(username = data)
	request.session['username'] = account.username
	request.session['idaccount'] = account.id
	request.session['firstname'] = account.first_name
	request.session['lastname'] = account.last_name
	request.session['email'] = account.email

# check authentification user session
def Check_session(request):
	response = False
	if request.session.get('username'):
		response = True
		
	return response

def Delete_session(request):
	try:
		del request.session['name']
		del request.session['password']
		del request.session['username']
		del request.session['idaccount']
		del request.session['firstname']
		del request.session['lastname']
		del request.session['email']
		del request.session['friendid']
	except KeyError:
		pass

def getimage(request):
	# get user image every redirect into another function

def Statusoffriends(me, you) :
	# check follower status based on user id 

def Searchdata(request, statusnavbar, keyword):
	# searching data from search box based on location user

# json operation for likes, collect and comment
def Likepost(request):
	# like another user post
	
def Collectpost(request):
	# collect saved post data 
	
def Createcomment(request):
	# make a comment in another users post
	
def Deletecomment(request, id):
	# delete user comment on post based on id

def Createforumcomment(request):
	# create user article comment on forum based on id

def Loadmoredata(request):
	# load more data based on user request and have a function like pagination via django

def Deleteforumcomment(request, id):
	# delete user article comment
	
@login_required(login_url='login')
def Finduser(request, username):
	# find another user account from search engine

def Followuser(request, id, status):
	# check user follower status

@login_required(login_url='login')
def Profile(request):
	# redirect user into their profile
		
@login_required(login_url='login')
def Collectiondata(request):
	# redirect user into their saved post data

# Settings menu
@login_required(login_url='login')
def Editprofile(request):
	# edit user profile

# source : https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
@login_required(login_url='login')
def Changepassword(request):
	if request.method == 'POST':
		Bpassword = request.POST.get('password1')
		Rpassword = request.POST.get('password2')
		if Bpassword == Rpassword:
			user = User.objects.get(id = request.session.get('idaccount'))
			user.set_password(Bpassword)
			user.save()
			update_session_auth_hash(request, user) 
			now = datetime.datetime.now()
			History.objects.create(userID = user, created_at = now, activity = "user", desc = "Your has changed your password recently")
			messages.success(request, 'Your password was successfully updated!')
			return redirect('profile')
		else:
			messages.error(request, 'Your password is not match')
			return redirect('changepassword')
	else:
		photo = getimage(request)
		unreadnotification = request.user.notifications.unread().count()
		form = PasswordChangeForm(request.user)
		konten = {'form': form, 'title':'Change Password', 'notification':unreadnotification, 'photo' : photo, 'statusnavbar' : 'login'}
		return render(request, 'settings/changepassword.html', konten)

@login_required(login_url='login')
def Historyactivity(request):
	# check user activity

@login_required(login_url='login')
def Blocklist(request):
	# show all users blocklist based on id

# kalo bisa dipake buat search box juga (challenge)
def Searchenginedata(request):
	# search engine version 2
