from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)

    class Meta:
        db_table = "menu_item"
