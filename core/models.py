from django.db import models

# Create your models here.
class Node(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_node = models.ForeignKey('self', on_delete=models.CASCADE,related_name='children', null=True, blank=True)

    def get_children(self):
        return self.children.all()

    def __str__(self) -> str:
        return str(self.name)