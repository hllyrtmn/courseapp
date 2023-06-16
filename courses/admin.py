from django.contrib import admin

from courses.models import Course,Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category_list")
    list_display_links = ("title","slug",)
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",),}
    list_filter = ("title","isActive",)
    list_editable= ("isActive",)
    search_fields = ("title","description",)

    def category_list(self,obj):
        html=""
        for category in obj.categories.all():
            html += category.categoryName + " "
        return html



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName","course_count")
    prepopulated_fields = {"slug":("categoryName",),}

    def course_count(self,obj):
        return obj.course_set.count()


# admin.site.register(Course,CourseAdmin)
# admin.site.register(Category)


