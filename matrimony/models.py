from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

#https://www.youtube.com/watch?v=phGHOMpukbk&list=PLva9wMNinRL5y-S9HBrnp23SSopHbMKby&index=6
#https://www.youtube.com/watch?v=N0s5hGTBnVs&list=PLva9wMNinRL5y-S9HBrnp23SSopHbMKby&index=7
# Create your models here.
#If your model already have data and you create new models and sec it will show error. so you should use (null=True)

class Religion(models.Model):  #one to many relation ORM as one Religion contain of many people(profiles)
    name= models.CharField(max_length=100)
    def __str__(self): # self function is to call by name not by object1 like that
        return self.name

class Sect(models.Model): ##one to many relation ORM as one Religion contain of many sections like shia & suni 
    name= models.CharField(max_length=100)
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='sects') # Foreign key create in many model and then cal single model init
    def __str__(self):
        return self.name

class Caste(models.Model): # one to many as many profiles has one cast
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Hobbies(models.Model): #many to many relation with profile model as multipe hobbies are in same profile or multiple profile has same hobby
    name= models.CharField(max_length=100)
    
    class Meta: #by default in django admin it shows 'hobbys' which is wrong spells u can correct bt this
        verbose_name_plural="Hobbies"
    
    def __str__(self):
        return self.name
    
class FatherProfile(models.Model): # one to one model relation
    name=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100,null=True, blank=True) #if not want to define
    def __str__(self):
        return self.name


class Profile(models.Model):
    GENDER_COICES=[
        ('M','Male'),
        ('F','Female'),
    ]
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(null=True, blank=True)   # pip install Pillow
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_COICES)
    occupation=models.CharField(max_length=100,null=True, blank=True) #if not want to define
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(max_length=254, unique=True) #unique email for every new data
    
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='profiles', null=True) # related_name='profiles' is to show profiles of same religion in religion model
    Sect=models.ForeignKey(Sect, on_delete=models.CASCADE, related_name='profiles', null=True)
    caste=models.ForeignKey(Caste, on_delete=models.CASCADE, related_name='profiles', null=True) #for one to many relation Foreign key used. Foreign key create in many model and then cal single model init
    hobbies=models.ManyToManyField(Hobbies, related_name='profiles') #many to many relation could be ad in any of model
    father=models.OneToOneField(FatherProfile, related_name='dependent', on_delete=models.CASCADE, null=True, blank=True) # related_name='dependent'. show with dependent name tablr in FatherProfile model
    
    def save(self, *args, **kwargs):  #when click on save button following task shown to user
        print(f"Data Updated for {self.name}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name