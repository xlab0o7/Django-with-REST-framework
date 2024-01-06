from django.db import models

# Create your models here.


class Books(models.Model):
    book_id = models.IntegerField(unique=True)
    book_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=150)

    def __str__(self):
        return self.book_name + "  ----  " + self.book_title


class Students(models.Model):
    student_name = models.CharField(max_length=50)
    student_age = models.PositiveIntegerField()
    student_dob = models.DateField()

    def __str__(self) -> str:
        return super().__str__().student_name
