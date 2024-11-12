from django.db import models
from apps.clients.models import Customer

class Order(models.Model): 
    order_id = models.IntegerField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, null=False)
    
    class Meta:
        db_table = "order"
        
    def __str__(self):
        return self.name
