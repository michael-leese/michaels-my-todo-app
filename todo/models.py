from django.db import models

# Create your models here.
class Item(models.Model):
    # Create the Item model for the DB
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    
    def __str__(self):
        return f"ID:{self.id} -> {self.name}"
    