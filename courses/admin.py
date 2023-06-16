from django.contrib import admin

from courses.models import Course,Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug")
    list_display_links = ("title","slug",)
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("title","isActive",)
    list_editable= ("isActive",)
    search_fields = ("title","description",)




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("categoryName",),}


# admin.site.register(Course,CourseAdmin)
# admin.site.register(Category)


