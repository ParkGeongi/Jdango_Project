from django.db import models

# Create your models here.
class Suser(models.Model):
    use_in_migration = True
    suser_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    point = models.TextField()
    class Meta:
        db_table = 'shop_users'
    def __str__(self):
        return f'{self.suser_id} {self.email} {self.nickname} {self.password} {self.point}'
