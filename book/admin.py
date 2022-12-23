from django.contrib import admin
# Register your models here.


from book.models import Category

class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category,categoryAdmin)