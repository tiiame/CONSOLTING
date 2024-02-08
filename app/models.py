from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Banner(models.Model):
    image = models.ImageField(upload_to="Banner")
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title

class Static(models.Model):
    count_students =models.IntegerField(default=1)
    count_university = models.IntegerField(default=1)
    year_of_experienced = models.IntegerField(default=1)
    count_countries = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.count_students

class Servic(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    icon = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title

class Results(models.Model):
    image = models.ImageField(upload_to="Results")
    name = models.CharField(max_length=100)
    name_institute = models.CharField(max_length=100)
    degree = models.IntegerField(default=100)

    def __str__(self) -> str:
        return self.name

class contakt(models.Model):
    class DegreeChoice(models.TextChoices):
        BACHELOR = "bachelor", "Bakalavr"
        MASTER = "master", "Master"
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    choice_institution = models.CharField(choices=DegreeChoice.choices,default=DegreeChoice.BACHELOR,max_length=100)
    telefon_number = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self) -> str:
        return self.first_name


class review(models.Model):
    image = models.ImageField(upload_to="Results/")
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class social(models.Model):
    icon = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    link = models.URLField()        

    def __str__(self) -> str:
        return self.icon









