import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from StudentApp.models import product

#import login required for login required session method
#..import login if doing django session
# Create your views here.
def index(request):
    return render(request,'home.html')
def usersignup(request):
    return render(request,'signup.html')
def loginpage(request):
    return render(request,'loginpage.html')
#@login_required(login_url='login')   #...login_required method
def student(request):
    if request.user.is_authenticated:       #...django session
    #if 'uid' in request.session:   #..simple session
        return render(request,'student.html')
    return render(request,'loginpage.html')   
  

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['usernamee']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email_id=request.POST['email_id']
        print(email_id)

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user already exists')
                return redirect('/')
            else:    
                user=User.objects.create_user(first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email_id)
                user.save()
                print('suceed')
                return redirect('loginpage')
        else:
            messages.info(request,'password not matching')        
        return redirect('usersignup')
def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']   
        user=auth.authenticate(username=username,password=password)
        #request.session['uid']=user.id
        #   #...simple session#
        if user is not None:
            login(request,user) #..django session...
            auth.login(request,user)
            messages.info(request,f'WELCOME {username}')
            return redirect('student')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('loginpage')  
    else:
        return render('loginpage') 
# #....#...login_required method
def logout(request):
    if request.user.is_authenticated: 
       auth.logout(request)
    return render(request,'home.html')  


def add(request):
    return render(request,'add_product.html')

def add_product(request):
    if request.method=='POST':
        pname=request.POST['product_name']
        qty=request.POST['quantity']
        price=request.POST['price']
        #simage=request.FILES['file']
        if request.FILES.get('file') is not None:
            simage=request.FILES['file']
        else:
            simage="/static/images/83.jpg"

        product1=product(product_name=pname,quantity=qty,price=price,image=simage)
        print('save')
        product1.save()

        return redirect('show_products')

def show_products(request):
   products=product.objects.all()
   return render(request,'showbase.html',{'products':products})         

def editpage(request,id):
    products=product.objects.get(id=id)
    return render(request,'edit.html',{'products':products}) 
#edit page..
def edit_product_details(request,id):
    if request.method=='POST':
        products=product.objects.get(id=id)
        products.product_name=request.POST.get('product_name')
        products.quantity=request.POST.get('quantity')
        products.price=request.POST.get('price')
        # products.image=request.FILES.get('file')
        if request.FILES.get('file') is not None:
            print(products.image)
            if products.image== "/static/images/83.jpg":
                # os.remove(products.image.path)
                products.image=request.FILES['file']
            else:
                os.remove(products.image.path)
                products.image=request.FILES['file']    
        else:
            os.remove(products.image.path)
            products.image="/static/images/83.jpg"        
        products.save()
        return redirect('show_products')
    return render(request,'edit.html') 
def delete(request,id):
    prd=product.objects.get(id=id)
    prd.delete()
    return redirect('show_products')    


  
                                 
