from django.db import models
class Test(models.Model):
    FileID = models.IntegerField(primary_key=True)
    FileRoot = models.CharField(max_length=64, default=None)
    FileInfo = models.CharField(max_length=30, default=None)
    Date = models.DateField(default=None)
    Location = models.CharField(max_length=10, default=None)
    FUpload = models.CharField(max_length=10, default=None)
    FClass = models.CharField(max_length=10, default=None)
    UserID = models.CharField(max_length=20, default=None)

