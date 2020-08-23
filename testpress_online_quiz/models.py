from django.db  import models 

class Exam(models.Model):
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct=models.CharField(max_length=100)

    class Meta:
        db_table="onlinequiz"