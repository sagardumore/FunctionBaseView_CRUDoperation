from django.db import models

# Create your models here.
#ra = (('2GB','2GB'),('4GB','4GB'),('8GB','8GB'),('16GB','16GB'),('32GB','32GB'))
#ro = (('500gb','500gb'),('1TB','1TB'),('2TB','2TB'),('3TB','3TB'),('4TB','324TB'))
pro = (('intel','INTEL'),('AMD Ryzen','AMD Ryzen'))
class Laptop(models.Model):
    company=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    ram=models.IntegerField()
    rom=models.IntegerField()
    processor=models.CharField(max_length=100,choices=pro)
    price = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.company}"