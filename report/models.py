from django.db import models


class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Ingredient', max_length=200, null=False, blank=False, default='New entry')
    description = models.TextField()
    Avg_weight = models.FloatField(blank=False, null=False, default='25')

    def __str__(self):
        return '{}/{}'.format(self.id, self.name, self.description)


class Report(models.Model):
    id = models.OneToOneField(Ingredients, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField('Ingredient', max_length=200, null=False, blank=False, default='New entry')
    opening_bgs = models.BigIntegerField(null=True, blank=True)
    opening_kgs = models.FloatField(null=True, blank=True)
    received = models.BigIntegerField(null=True, blank=True)
    bags_used_bin = models.BigIntegerField(null=True, blank=True)
    bags_used_Th3 = models.BigIntegerField(null=True, blank=True)
    kgs_used_Th3 = models.FloatField(null=True, blank=True)
    lot_number = models.CharField(max_length=200, null=True, blank=True)
    current_bgs = models.BigIntegerField(null=True, blank=True)
    current_kgs = models.FloatField(null=True, blank=True)
    total_used_kgs = models.FloatField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    comment_body = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}/{}'.format(self.id, self.name, self.opening_kgs, self.received, self.bags_used_bin, self.bags_used_Th3, self.lot_number, self.current_bgs, self.current_kgs, self.total_used_kgs, self.expiry_date)

