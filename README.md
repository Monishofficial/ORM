# Ex03 Django ORM Web Application
## Date: 18/09/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-09-18 092353.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py 
from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
	Loan_no=models.IntegerField(primary_key=True);
	Name=models.CharField(max_length=30);
	Account_no=models.IntegerField();
	Loan_amt=models.IntegerField();
	Mobile_number=models.IntegerField();
class BankloanAdmin(admin.ModelAdmin):
	list_display=("Loan_no","Name","Account_no","Loan_amt","Mobile_number");

admin.py
  
from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)
```


## OUTPUT
![alt text](<Screenshot (114).png>)

 
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
