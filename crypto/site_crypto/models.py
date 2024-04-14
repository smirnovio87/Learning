from django.db import models
import os
import uuid
class Exchange (models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20, verbose_name="Название Биржы")
    location = models.CharField(max_length=250, verbose_name="Адрес биржы")
    trade_volume = models.FloatField(verbose_name="Объем торгов")
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = "Биржа"
        verbose_name_plural = "Биржи"
