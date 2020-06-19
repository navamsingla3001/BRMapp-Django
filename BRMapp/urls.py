from django.conf.urls import url
from BRMapp import views
from django.urls import path

urlpatterns=[
    url('view-book', views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('search-book',views.searchBook),
    url('new-book',views.newBook),
    url(r'^add',views.add),
    url('search',views.search),
    url('edit',views.edit),
    url('login',views.userlogin),
    url('logout',views.userLogout),

]
