from django.db import models


class Tree(models.Model):
    db_table = 'tree'
    date_created = models.DateField(auto_now_add=False, null=False)
    folder_path = models.CharField(max_length=40, blank=False, null=False)
    key = models.CharField(max_length=100, blank=False, null=False)
