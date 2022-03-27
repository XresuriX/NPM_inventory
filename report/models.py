from django.db import models


class Ingredients(models.Model):
    id = models.ForeignKey(primary_key=True, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.id, self.name, self.description)


class Report(models.Model):
    id = models.BigAutoField(Ingredients, on_delete=models.CASCADE, primary_key=True)
    opening_bgs = models.BigIntegerField(null=True, blank=True)
    opening_kgs = models.FloatField(null=True, blank=True)
    recieved = models.BigIntegerField(null=True, blank=True)
    bags_used_bin = models.BigIntegerField(null=True, blank=True)
    bags_used_Th3 = models.BigIntegerField(null=True, blank=True)
    kgs_used_Th3 = models.FloatField(null=True, blank=True)
    lot_number = models.CharField(max_length=200, null=True, blank=True)
    current_bgs = models.BigIntegerField(null=True, blank=True)
    current_kgs = models.FloatField(null=True, blank=True)
    total_used_kgs = models.FloatField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    comment_body = models.TextField()

    def __str__(self):
        return '%s %s' % (self.id, self.opening_kgs, self.recieved, self.bags_used_bin, self.bags_used_Th3, self.lot_number, self.current_bgs, self.current_kgs, self.total_used_kgs, self.expiry_date)


