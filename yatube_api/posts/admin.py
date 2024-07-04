from django.contrib import admin

from posts.constants import LIST_PER_PAGE
from posts.models import Comment, Group, Post


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
    list_per_page = LIST_PER_PAGE
    search_fields = ('text',)

    @admin.display(description='Количество комментариев')
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

    @admin.display(description='Количество записей')
    def count_posts(self, object):
        return object.posts.count()


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
    list_per_page = LIST_PER_PAGE
    search_fields = ('text',)


admin.site.site_title = 'Администрирование Yatube'
admin.site.site_header = 'Администрирование Yatube'
