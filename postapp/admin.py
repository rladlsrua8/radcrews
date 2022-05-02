from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = (
        'title',
        'content',
        'writer',
        'hits',
        'tag_list',
        'modify_dt',

    )
    list_filter = ('modify_dt',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())