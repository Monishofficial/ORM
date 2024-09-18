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