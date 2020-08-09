from django.db import models


class ItemRate(models.Model):
    item = models.CharField(max_length=255)
    date = models.DateField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.item}-{self.date}-{self.rate}'
