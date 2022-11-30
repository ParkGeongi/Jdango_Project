from django.db import models

# Create your models here.
class movie_user(models.Model):
    use_in_migration = True
    user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.IntegerField()

    class Meta:
        db_table = 'movie_users'
    def __str__(self):
        return f'{self.user_id} {self.email} {self.nickname} {self.password} {self.age}'

