from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name

class ChildCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="childcategories")

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    childcategory = models.ForeignKey(ChildCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.CharField(blank=True, null=True)
    is_active = models.BooleanField(default=True)  # Active or inactive status


    def __str__(self):
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField()
    password2 = models.CharField()
   

class DBdata(models.Model):

    email = models.CharField(unique=True)
    password= models.CharField(max_length=200)
    
