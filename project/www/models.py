from django.db import models




class Industry(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    mail = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='images')
    industry = models.ManyToManyField(Industry)
    text = models.CharField(max_length=150)


    def __str__(self):
        return self.name + " " + self.surname