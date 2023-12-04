from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        # Add this line to set a custom primary key
        default_auto_field = 'django.db.models.AutoField'
