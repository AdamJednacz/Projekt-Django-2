from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    mail = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    price = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='images')
    industry = models.ManyToManyField(Industry)
    text = models.CharField(max_length=150)


    def __str__(self):
        return self.name + " " + self.surname
    

class AcceptedOffer(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    mail = models.EmailField(100)
    number = models.CharField(max_length=12)
    price = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='photos/')
    text = models.TextField()
    industry = models.ManyToManyField(Industry)
    def __str__(self):
       return self.name + " " + self.surname
    

    
class Like(models.Model):
    accept_offer = models.ForeignKey(AcceptedOffer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    def __str__(self):
        return f'Like on {self.accept_offer }'

class Unlike(models.Model):
    accept_offer  = models.ForeignKey(AcceptedOffer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    def __str__(self):
        return f'Unlike on {self.accept_offer }'    