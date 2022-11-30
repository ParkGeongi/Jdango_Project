from django.db import models

# Create your models here.
class Comment(models.Model):
    use_in_migration = True
    comment_id = models.AutoField(primary_key=True)
    ccontent = models.TextField()
    ccreated_at = models.DateTimeField()
    cupdated_at = models.DateTimeField()


    class Meta:
        db_table = 'blog_comments'
    def __str__(self):
        return f'{self.comment_id} {self.ccontent} {self.ccreated_at} {self.cupdated_at}'