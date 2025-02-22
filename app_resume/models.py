from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Resume(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    job_title = models.CharField(max_length=60 , null = True)
    about = models.TextField(null = True)
    field = models.CharField(max_length=60 , null = True)
    
    def __str__(self):
        
        return self.user.username
    
    
class work_experience(models.Model):
    Resume = models.ForeignKey(Resume , on_delete =models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    title = models.CharField(max_length=60 , null = True)
    company_name = models.CharField(max_length=60 , null = True)

    def __str__(self):
        return self.title or ''