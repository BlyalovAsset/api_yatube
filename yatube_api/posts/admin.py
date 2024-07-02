from django.contrib import admin

from posts.models import Comment, Follow, Group, Post
from posts.constants import list_per_page

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'image',
        'pub_date',
        'author',
        'group',
        'count_comments',
    )
    
    admin.site.empty_value_display
    list_editable = ('group',)
    list_filter = ('pub_date',)
    list_per_page
    search_fields = ('text',)

    @admin.display(short_description = 'Количество комментариев')
    def count_comments(self, object):
        return object.comments.count()


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
        'count_posts'
    )
    empty_value_display = '-пусто-'
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def count_posts(self, object):
        return object.posts.count()

    count_posts.short_description = 'Количество записей'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'post',
        'author',
        'text',
        'created'
    )

    list_editable = ('author',)
    list_filter = ('author',)
    list_per_page
    search_fields = ('text',)


admin.site.site_title = 'Администрирование Yatube'
admin.site.site_header = 'Администрирование Yatube'
