from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class movie_cinemas(models.Model):
    use_in_migration = True
    cinema_id = models.AutoField(primary_key=True)
    ctitle = models.TextField()
    image_url = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()

    class Meta:
        db_table = 'movie_cinemas'
    def __str__(self):
        return f'{self.cinema_id} {self.ctitle}  {self.image_url} {self.address} {self.detail_address}'