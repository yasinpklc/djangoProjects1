from django.contrib import admin
# Register your models here.


from Library.models import Category,Library

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['status']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Library)
