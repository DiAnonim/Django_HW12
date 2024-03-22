from django.db import models

class AbstractBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    publisher = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True

class Book(AbstractBook):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
