
from django.db import models


class GBPEUR(models.Model):
    pub_date = models.DateTimeField('date published')
    #This field might not be necessary if currency pairs are saved in separate tables.
    currency_pair = models.CharField(max_length=200)
    fx_value = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)


# fx_value = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)

