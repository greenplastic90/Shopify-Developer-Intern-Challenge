from django.db import models

# Create your models here.


class InventoryItem(models.Model):
    name = models.CharField(max_length=100, default=None)
    warehouse = models.ForeignKey('warehouses.Warehouse',
                                  related_name="inventory_items",
                                  on_delete=models.DO_NOTHING)


def __str__(self):
    return f"{self.name}"
