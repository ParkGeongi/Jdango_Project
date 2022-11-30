
from django.db import models

# Create your models here.
class View(models.Model):
    use_in_migration = True
    view_id = models.AutoField(primary_key=True)
    ip_address = models.TextField()
    vcreated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table = 'blog_views'
    def __str__(self):
        return f'{self.view_id} {self.ip_address} {self.vcreated_at}'