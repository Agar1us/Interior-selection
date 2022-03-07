from django.db import models

class Room(models.Model):

    name = models.CharField(unique=True, max_length=40)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='photos/%Y/%m')
    exist = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name


class Interior(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    exist = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name + ' | ' + self.room.name


class Displacement(models.Model):

    object = models.ForeignKey(to=Interior, on_delete=models.CASCADE)
    last_room = models.ForeignKey(to=Room, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.object.name + ' | ' + self.last_room.name + ' | ' + self.object.room.name + ' | ' + self.date

