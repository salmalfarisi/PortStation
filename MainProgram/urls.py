from django.urls import path, include
from django.conf.urls import url
import notifications.urls
from . import views 

urlpatterns = [
# General Content
    # recent post from community or user
    path('', views.SignIn, name="login"),
    path('logout/', views.Signout, name="logout"),
    path('register/', views.Register, name="register"),
#Users Activity
	# notifications
	url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # users profile and collection
	path('forgotpassword/', views.Forgotpassword, name="forgotpassword"),
	path('token/<str:verificationtoken>', views.Resetpassword, name="resetpassword"),
	path('email/send', views.Sendemail, name="email"),
    path('profile', views.Profile, name="profile"),
    path('collection', views.Collectiondata, name="collection"),
    # recent activity from friend list
    path('home', views.Home, name="home"),
	# likes, collect and comment for post
	path('post/likepost', views.Likepost, name="likepost"),
	path('post/commentpost/create', views.Createcomment, name="makecomment"),
	path('post/commentpost/delete/<int:id>', views.Deletecomment, name="deletecomment"),
	path('post/collectpost', views.Collectpost, name="collecpost"),
	# cookie and session
	path('testcookie/', views.Cookie_session, name="cek_cookie_session"),
	path('deletecookie/', views.Cookie_delete, name="deleteCookie"),
	path('createsession/', views.Create_session, name="createSession"),
	path('deletesession/', views.Delete_session, name="deleteSession"),
	# CRUD for post
	path('post/create', views.Createpost, name="createpost"),
	path('post/show/<int:id>', views.Showpost, name="detailpost"),
	path('post/edit/<int:id>', views.Editpost, name="editpost"),
	path('post/delete/<int:id>/<currenturl>', views.Deletepost, name="deletepost"),
	# CRUD for Forum Discussion
	path('forum/index', views.Indexforum, name="indexforum"),
	path('forum/create', views.Createforum, name="createforum"),
	path('forum/show/<int:id>', views.Showforum, name="detailforum"),
	path('forum/edit/<int:id>', views.Editforum, name="editforum"),
	path('forum/delete/<int:id>', views.Deleteforum, name="deleteforum"),
	# comment for forum
	path('forum/commentforum/create', views.Createforumcomment, name="makeforumcomment"),
	path('forum/commentforum/delete/<int:id>', views.Deleteforumcomment, name="deleteforumcomment"),
	# searching data via search box
	path('searching/<str:statusnavbar>/<str:keyword>', views.Searchdata, name="searchdata"),
	path('searching/', views.Searchenginedata, name="searchenginedata"),
	# following user system
	path('users/<str:username>', views.Finduser, name="findaccount"),
	path('users/<int:id>/<str:status>', views.Followuser, name="followuser"),
	# settings menu
	path('setting/profile', views.Editprofile, name="editprofile"),
	path('setting/blocklist', views.Blocklist, name="blocklist"),
	path('setting/history', views.Historyactivity, name="history"),
    path('setting/password', views.Changepassword, name='changepassword'),
	# multi function
	path('loaddata', views.Loadmoredata, name="loadmoredatas"),
]