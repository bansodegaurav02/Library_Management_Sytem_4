from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth import authenticate,login,logout
import requests
from django.http import JsonResponse
from .models import *

from .forms import *

from django.contrib import messages

def import_books(request):

    url = f"https://frappe.io/api/method/frappe-library?page={1}"  # URL of the Frappe API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('message', [])
        
        context={'data':data}
       

    return render(request,'add_book.html',context)


def page_sort(request):
    if request.method=='POST':
        page_data=request.POST['page_no']

        url = f"https://frappe.io/api/method/frappe-library?page={page_data}"  # URL of the Frappe API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get('message', [])
        
            context={'data':data}
       

    return render(request,'add_book.html',context)




def add_library(request,title):


    url = "https://frappe.io/api/method/frappe-library"  # URL of the Frappe API
    parameters = {
        
        'title': f'{title}'  # Example parameter, you can adjust this as needed
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json().get('message', [])
        for book_data in data:
            
            title1 = book_data.get('title', '')
            author = book_data.get('authors', '')
            isbn = book_data.get('isbn', '')
            publisher=book_data.get('publisher','')
            num_pages=book_data.get('num_pages','')




            existing_book = Book.objects.filter(isbn=isbn).first()
            if existing_book:
                existing_book.quantity += 30
                existing_book.save()
            else:
                Book.objects.create(title=title1, author=author, isbn=isbn,publisher=publisher,page=num_pages)

        messages.success(request,'Succesfully Book Added TO Library')
        return redirect('book_details')
    else:
        messages.error(request,'Something Went Werong !')
        return redirect('add_to_library')
        

    
    
    

    

def add_issuer(request):

    if request.method=="POST":
        fm=issue_form(request.POST)
        if fm.is_valid():
            data = fm.cleaned_data["book"]

            obj=Book.objects.get(title=data)
            if obj:
                obj.quantity -= 1
                obj.save()

            fm.save()
            messages.success(request,'Succesfully Add Issuer')
            return redirect('book_details')
            


    else:
        fm=issue_form()

    context={'fm':fm}

    return render(request,'add_isuer.html',context)




def show_issuer_details(request):
    obj=Transaction.objects.all()

    return render(request,'show_issuer.html',{'data':obj})



def book_details(request):

    obj=Book.objects.all()

    return render(request,'book_details.html',{'data':obj})


def Book_return(request,id,title):
    obj1=Transaction.objects.get(id=id)
    obj1.delete()

    obj=Book.objects.get(title=title)
    if obj:
        obj.quantity += 1
        obj.save()
    
    return redirect('book_details')




    

def update_issuer(request,id):

    if request.method=="POST":
        obj1=Transaction.objects.get(id=id)
        obj=issue_form(request.POST,instance=obj1)
        obj.save()
        messages.success(request,'Succesfully Updating data')
        return redirect('book_details')

    else:
        obj1=Transaction.objects.get(id=id)
        obj=issue_form(instance=obj1)  



    context={'obj':obj,'fm':obj,'obj1':obj1}


    return render(request,'add_isuer.html',context)




def search_books(request):
     if request.method=='POST':
        value=request.POST['book']
        data=Book.objects.filter(title__contains=value)
        context={'data':data}
        return render(request,'book_details.html',context)
     



def Register(request):

    if request.method=="POST":
        fm=userregistration(request.POST)
        if fm.is_valid():
            data = fm.cleaned_data["first_name"]
            data2=fm.cleaned_data["last_name"]
            obj=Member.objects.create(name=f'{data} {data2}')
            obj.save()


            fm.save()
            messages.success(request,'Succesfully Register')


            return redirect('login_info')

        else:
            messages.error(request,'Something Went Wrong !')


    else:
        fm=userregistration()

    context={'fm':fm}

    return render(request,'Register.html',context)






def login_info(request):

    if request.method=='POST':
        uname=request.POST['username']
        upasss=request.POST['password']

        user=authenticate(request,username=uname,password=upasss)

        if user is not None:
            login(request,user)
            messages.success(request,'Succesfully Login')
            
            return redirect('book_details')
        else:
            messages.error(request,'Something Went Wrong !')

    
    return render(request,'login.html')
            
    



def log_out(request):
    logout(request)
    
    return redirect('book_details')



def delete_book(request,id):
    obj=Book.objects.get(id=id)
    obj.delete()
    messages.success(request,'Succesfully Deleted')
    return redirect('book_details')