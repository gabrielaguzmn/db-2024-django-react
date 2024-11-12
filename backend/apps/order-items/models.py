from django.db import models
from apps.order.models import Order
from apps.product.models import Product

class OrderItem(models.Model): 
    order_item_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        db_table = "order_items"
        
    def __str__(self):
        return self.name
