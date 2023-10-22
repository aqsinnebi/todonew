from django.db import models
import datetime

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    priority =models.DateTimeField(null=True)
    created_at = models.DateTimeField( auto_now=True, null=True, )
   
    
  
    
    
    
    

