from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, PostTour

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id','title', 'category', 'date_created', 'user')
    list_display_links = ('id', 'title', 'user')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(PostTour, BlogPostAdmin)
