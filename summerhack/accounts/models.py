from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save

class Tree(models.Model):
    db_table = 'tree'
    date_created = models.DateField(auto_now_add=False, null=False)
    folder_path = models.CharField(max_length=40, blank=False, null=False)
    key = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.user.username

    def create_tree(sender, instance, created, **kwargs):
        if created:
            tree = Tree()
            tree.folder_path = instance
            tree.save(update_fields=['folder_path'])

    post_save.connect(create_tree, sender=User)


