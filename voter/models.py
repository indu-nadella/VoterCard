from django.db import models

# Create your models here.
class Voter(models.Model):
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    ]
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    address=models.TextField()
    photo=models.ImageField(upload_to='photo')
    voter_id=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name
