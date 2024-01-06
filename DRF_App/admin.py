from django.contrib import admin

from DRF_App.models import Books, Students

# Register your models here.


@admin.register(Books)
class Book(admin.ModelAdmin):
    list_display = ["book_id", 'book_name', 'book_title']


@admin.register(Students)
class Student(admin.ModelAdmin):
    list_display = [
        'student_name', 'student_age', 'student_dob'
    ]
