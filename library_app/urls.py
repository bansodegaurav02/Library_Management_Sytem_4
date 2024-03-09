"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_books',views.import_books,name='home'),
    path('delete_book/<id>',views.delete_book,name='delete_book'),
   
    path('add_to_library/<str:title>',views.add_library,name='add_to_library'),
    path('add_issuer/',views.add_issuer,name='add_issuer'),
    path('show_issuer/',views.show_issuer_details,name='show_issuer'),
    path('',views.book_details,name='book_details'),
    path('page_sort/',views.page_sort,name='page_sort'),
    path('Book_return/<id>/<str:title>',views.Book_return,name='Book_return'),
    path('update_issuer/<id>',views.update_issuer,name='update_issuer'),
    path('search_books/',views.search_books,name='search_books'),
    path('Register/',views.Register,name='Register'),
    path('login_info/',views.login_info,name='login_info'),
    path('log_out',views.log_out,name='log_out'),



    
]
