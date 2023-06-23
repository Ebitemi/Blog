from django.contrib import admin
from .models import Staff
from .models import BlogPost, Categories, Opportunity, OpportunityPost, Memes, Jokes, Event, InternshipPost,JobPost, ScholarshipPost 

admin.site.register(Staff)
admin.site.register(BlogPost)
admin.site.register(Categories)
admin.site.register(Opportunity)
admin.site.register(OpportunityPost)
admin.site.register(InternshipPost)
admin.site.register(JobPost)
admin.site.register(ScholarshipPost)
admin.site.register(Memes)
admin.site.register(Jokes)
admin.site.register(Event)
