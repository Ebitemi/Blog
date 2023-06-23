from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Blog_Home"),
    
    path("authentication/register" , views.Regform, name="register"),
    path("authentication/login", views.login_form, name ="login"),
    
    # The main blog views
    path("base2/" , views.base2, name="Blog_About"),
    path("user-login", views.user_login, name ="user-login"),
    path("signup", views.signUp, name ="signup"),
    path("base2/contact-us", views.contact, name ="contact-us"),
    path("base2/blog_details/<int:id>", views.blogDetails, name ="blog_details"),
    path("base2/blog-grid", views.blogGrid, name ="blog-grid"),
    path("base2/bootcamps", views.bootcamps, name ="bootcamps"),
    path("base2/internships", views.internships, name ="internships"),
    path("base2/scholarships", views.scholarships, name ="scholarships"),
    path("base2/jobs", views.jobs, name ="jobs"),
    path("base2/tips", views.tips, name ="tips"),
    path("base2/tutorials", views.tutorials, name ="tutorials"),
    path("base2/frontend", views.frontend, name ="frontend"),
    path("base2/backend", views.backend, name ="backend"),
    path("base2/fullstack", views.full_stack, name ="fullstack"),
    path("base2/wordpress", views.word_press, name ="wordpress"),
    path("base2/backend", views.backend, name ="backend"),
    path("base2/jokes", views.jokes, name ="jokes"),
    path("base2/memes", views.memes, name ="memes"),
    path("base2/events", views.events, name ="events"),
    path("base2/privacy", views.privacy, name ="privacy"),
    path("base2/terms", views.terms, name ="terms"),
]
