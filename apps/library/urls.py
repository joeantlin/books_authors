from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^newbook$', views.newbook),
    url(r'^authors$', views.authorpage),
    url(r'^newauthor$', views.newauthor),
    url(r'^books/(?P<book_num>\d+)$', views.books),
    url(r'^addauthor$', views.addauthor),
    url(r'^authors/(?P<author_num>\d+)$', views.authors),
    url(r'^addbook$', views.addbook),
]
