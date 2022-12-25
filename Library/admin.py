from django.contrib import admin
# Register your models here.
from Library.models import Category, Library, Images
class LibraryImageInline(admin.TabularInline):
    model = Images
    extra = 3
class CategoryAdmin(admin.ModelAdmin):
    List_display = ['title','status','image_tag']
    readonly_fields = ('image_tag',)
    List_filter = ['status']
class LibraryAdmin(admin.ModelAdmin):
    List_display = ['title','category','price','amount','image_tag','status']
    readonly_fields = ('image_tag',)
    List_filter = ['status','category']
    inlines = [LibraryImageInline]

class ImagesAdmin(admin.ModelAdmin):
    List_display = ['title','Library','image_tag']
    readonly_fields = ('image_tag',)
    List_filter = ['status']
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Images,ImagesAdmin)