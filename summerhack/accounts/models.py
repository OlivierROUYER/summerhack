from django.db import models


class Tree(models.Model):
    db_table = 'tree'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    folder_path = models.CharField(max_length=200, blank=False, null=False)
    key = models.CharField(max_length=100, blank=False, null=False)
    # compare = models.CharField(max_length=10, blank=False, null=False)
