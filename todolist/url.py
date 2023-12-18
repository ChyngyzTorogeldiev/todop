from django.conf.urls import url
from django.contrib import admin
from todolist.views import todo
from todolist.views import category
from todolist.views import redirect_view
 
urlpatterns = [
	url(r'$^', redirect_view ),
	url(r'^admin/', admin.site.urls),
	url(r'^todo/', todo, name="TodoList"),
	url(r'^category/', category, name="Category"),
]