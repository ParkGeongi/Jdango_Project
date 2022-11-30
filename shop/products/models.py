from django.db import models

# Create your models here.
class Product(models.Model):
    use_in_migration = True
    product_id = models.AutoField(primary_key=True)
    pname = models.TextField()
    price = models.IntegerField()
    image_url = models.TextField()

    class Meta:
        db_table = 'shop_products'

    def __str__(self):
        return f'{self.product_id} {self.pname} {self.price} {self.image_url}'
