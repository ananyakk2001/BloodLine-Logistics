from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class Blood(models.Model):
    blood_name = models.CharField(max_length=100,default=1)

class Donor(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    BLOOD_ID = models.ForeignKey(Blood, default=1, on_delete=models.CASCADE)
    house = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, default=1)
    age=models.CharField(max_length=100, default=1)


class Seeker(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    BLOOD_ID = models.ForeignKey(Blood, default=1, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)


class Request(models.Model):
    SEEKER = models.ForeignKey(Seeker, default=1, on_delete=models.CASCADE)
    date = models.DateField(max_length=100)
    quantity = models.CharField(max_length=100, default=1)
    status = models.CharField(max_length=100)
    BLOOD_ID = models.ForeignKey(Blood, default=1, on_delete=models.CASCADE)

class Request_allocation(models.Model):
    DONOR = models.ForeignKey(Donor, default=1, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(Request, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Feedback(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)




class Blood_bank(models.Model):
    BLOOD_ID = models.ForeignKey(Blood, default=1, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)







