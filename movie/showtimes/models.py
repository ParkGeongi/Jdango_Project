from django.db import models

# Create your models here.
class movie_showtime(models.Model):
    use_in_migration = True
    showtime_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movie_show_times'
    def __str__(self):
        return f'{self.showtime_id} {self.start_time} {self.end_time}'
