from django.db import models
# {id: 1, name: 'Имя', title: 'Бла-Бла', money: 1000, popularity: 0, army: 0, land: -10},
class Cards(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=False,default="")
    title = models.TextField(blank=True, null=False,default="")
    money=models.IntegerField(blank=True, null=False,default=0)
    popularity = models.IntegerField(blank=True, null=False, default=0)
    army = models.IntegerField(blank=True, null=False, default=0)
    land = models.IntegerField(blank=True, null=False, default=0)
    rare = models.IntegerField(blank=True, null=True, default=1)
    is_learn=models.BooleanField(blank=True, null=False, default=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        managed = True
        db_table = 'cards'

class Num_edu(models.Model):
    id = models.BigAutoField(primary_key=True)
    desc= models.TextField(blank=True, null=False,default="")
    epo=models.IntegerField(blank=True, null=False,default=100)
    card_num=models.IntegerField(blank=True, null=False,default=0)
    error=models.FloatField(blank=True, null=False,default=0)
    dif_money=models.IntegerField(blank=True, null=False,default=100000)
    dif_popularity = models.IntegerField(blank=True, null=False, default=1000)
    dif_army = models.IntegerField(blank=True, null=False, default=1000)
    dif_land = models.IntegerField(blank=True, null=False, default=1000)
    graph= models.TextField(blank=True, null=True)
    graph_num = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        managed = True
        db_table = 'models'

    def __str__(self):
        return str(self.id)


class Trys(models.Model):
    id = models.BigAutoField(primary_key=True)
    card_num=models.IntegerField(blank=True, null=False,default=0)
    epo=models.IntegerField(blank=True, null=False,default=100)
    desc = models.TextField(blank=True, null=False, default="")
    dif_money=models.IntegerField(blank=True, null=False,default=0)
    dif_popularity = models.IntegerField(blank=True, null=False, default=0)
    dif_army = models.IntegerField(blank=True, null=False, default=0)
    dif_land = models.IntegerField(blank=True, null=False, default=0)
    num = models.ForeignKey(Num_edu, on_delete=models.CASCADE, blank=True, null=True)
    graph= models.TextField(blank=True, null=True)
    graph_num = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
        managed = True
        db_table = 'trys'


class Kings(models.Model):
    id = models.BigAutoField(primary_key=True)
    solutions=models.TextField(blank=True, null=False, default="")
    Try = models.ForeignKey(Trys, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name = 'Король'
        verbose_name_plural = 'Короли'
        managed = True
        db_table = 'kings'
