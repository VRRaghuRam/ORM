from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
   accountno=models.IntegerField(primary_key="accountno")
   loantype=models.CharField(max_length=100)
   name=models.CharField(max_length=20)
   address=models.CharField(max_length=60)
   aadharno=models.IntegerField()
   

class BankloanAdmin(admin.ModelAdmin):
   list_display=("accountno","name","address","aadharno")
