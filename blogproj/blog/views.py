from django.shortcuts import render, HttpResponse,redirect
from . models import Staff, BlogPost, Categories, Memes, OpportunityPost, InternshipPost, ScholarshipPost, JobPost

from .forms import RegForm
from django.contrib.auth import login, authenticate

# Create your views here.

# The admin panel area
posts =[
    {
        'Author': "Temisan Ebireri",
        'Title': "Why You Act The Way You Do ?",
        'Content': "Stop Pretending not to know",
        'Date_Posted': "7th August, 2021 "
    },
    {
        'Author': "Naomi Gentle-idyee",
        'Title': "Why Makes You Happy ?",
        'Content': "It's always the little things",
        'Date_Posted': "10th October, 2020 "
    }
]
    
def home(request):
    context = {
        'posts': BlogPost.objects.all().order_by('id')[:3]
    }
    return render(request, 'blog/index.html', context)

def Regform(request):
    print("the method is ",request.method)
    if request.method == "POST":
        print("Hello")
        user = request.user
        staff = Staff.objects.get(user = user)
        if staff.is_admin == True:
            data = request.POST
            form = RegForm(data)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(data['password'])
                user.save()

                profile = Staff()
                profile.user = user
                profile.role = data['role']
                profile.save()

                return redirect("Blog_Home")
            else:
                return HttpResponse("<p>error</p>")
        else:
            return HttpResponse("<h1>unauthorized</h1>")

            #creating user staff profile
    return render(request, 'blog/register.html', {'title':"Reg form"})


# This is for the main blog area

def create_category(request):
    data = request.POST
    new_category = Categories()
    new_category.name = data['category']
    new_category.save()

    return redirect('home')

def base2(request):
    return render(request, 'blog/about.html', {'title':"About"})

def login_form(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        

        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("<h1>Login Successful</h1>")
            # return redirect('home')
        
        else:
            msg = "Invalid Username or Password"
    return render(request, "blog/log-in.html", {'msg':msg})

def signUp(request):
   
    if request.method == "POST":
        form = RegForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            if password == confirm_password:
                user.set_password(request.POST['password'])
                user.save()
        
                return redirect('user-login')
            else:
                return render(request, "blog/sign-in.html", {'msg':"Passwords did not match"})
        
        else:
            return render(request, "blog/sign-in.html", {'form':form})
        
    form = RegForm()
    return render(request, "blog/sign-in.html", {'form':form})

def user_login(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        

        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return HttpResponse("<h1>Login Successful</h1>")
            return redirect('Blog_Home')
        
        else:
            msg = "Invalid Username or Password"
    return render(request, "blog/log-in.html", {'msg':msg})

def contact(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/contact.html', context)

def blogGrid(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blog/blog-grid.html', context)

def blogDetails(request,id):
    blog =  BlogPost.objects.get(id=id)
    category = blog.category
    related_blog = BlogPost.objects.filter(category=category)
    context = {
        'post': blog,
        'related_post':related_blog
    }
    return render(request, 'blog/blog-details.html', context)

def bootcamps(request):
    context = {
        'posts': OpportunityPost.objects.all()
    }
    return render(request, 'blog/bootcamps.html', context)

def internships(request):
    context = {
        'posts': InternshipPost.objects.all()
    }
    return render(request, 'blog/internships.html', context)

def scholarships(request):
    context = {
        'posts': ScholarshipPost.objects.all()
    }
    return render(request, 'blog/scholarships.html', context)

def jobs(request):
    context = {
        'posts': JobPost.objects.all()
    }
    return render(request, 'blog/jobs.html', context)

def tips(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/tips.html', context)

def tutorials(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/tutorials.html', context)

def frontend(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/frontend.html', context)

def backend(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/backend.html', context)

def full_stack(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/fullstack.html', context)

def word_press(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/wordpress.html', context)

def jokes(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/jokes.html', context)

def memes(request):
    context = {
        'posts': Memes.objects.all()
    }
    return render(request, 'blog/memes.html', context)

def events(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/events.html', context)


def privacy(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/privacy.html', context)

def terms(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/terms.html', context)

