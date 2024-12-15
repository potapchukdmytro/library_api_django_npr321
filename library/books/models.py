from django.db import models

# Create your models here.
class TemplateModel(models.Model):
    text = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    body = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.text}; {self.email}"
    