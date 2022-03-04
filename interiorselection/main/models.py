from django.db import models
from PIL import Image

class Rooms(models.Model):

    name = models.CharField('Название комнаты', primary_key=True, max_length=40)
    image = models.ImageField('Фоторафия комнаты', null=True, blank=True, upload_to='photos/%Y/%m')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

class Interiors(models.Model):

    name = models.CharField('Предмет', max_length=50)
    room = models.ForeignKey(to=Rooms, null=True, on_delete=models.SET_NULL, verbose_name='Расположение',)

    def __str__(self):
        return self.name + ' | ' + self.room.name

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентарь'

class Displacement(models.Model):

    object = models.ForeignKey(to=Interiors, verbose_name='Инвентарь', on_delete=models.CASCADE)
    last_room = models.ForeignKey(to=Rooms, null=True, on_delete=models.SET_NULL, verbose_name='Прошлое расположение',)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время перемещения')

    def __str__(self):
        return self.object.name + ' | ' + self.last_room.name + ' | ' + self.object.room.name + ' | ' + self.date

    class Meta:
        verbose_name = 'Перемещение объекта'
        verbose_name_plural = 'Перемещение объекта'

