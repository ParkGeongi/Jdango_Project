from django.db import models

# Create your models here.
class Tag(models.Model):
    use_in_migration = True
    tag_id = models.AutoField(primary_key=True)
    title = models.TextField()


    class Meta:
        db_table = 'blog_tags'
    def __str__(self):
        return f'{self.pk} {self.title}'