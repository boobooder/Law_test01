from django.db import models

# Create your models here.
class Lawtable(models.Model):
    law_order = models.TextField(default="第n條")
    law_index = models.TextField(default="填入內容")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "LawSearch_table"