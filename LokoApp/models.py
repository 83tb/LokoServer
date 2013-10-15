from django.db import models

# Create your models here.


class Queue(models.Model):
    """
    Both Likwidators and Doctors can come from the certain region of Poland, this is the class that represents Region
    """



    command = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.command