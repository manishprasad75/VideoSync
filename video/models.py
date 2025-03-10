from django.db import models

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=644)
    filepath = models.FileField(upload_to="videos/", null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)
