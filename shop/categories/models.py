from django.db import models

# Create your models here.
class Category(models.Model):
    use_in_migration = True
    category_id = models.AutoField(primary_key=True)
    cname = models.TextField()


    class Meta:
        db_table = 'shop_categories'

    def __str__(self):
        return f'{self.category_id} {self.cname}'
