from django.db import models

# Create your models here.


class Books(models.Model):
    book_id = models.IntegerField(unique=True)
    book_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=150)

    def __str__(self):
        return self.book_name + "  ----  " + self.book_title
