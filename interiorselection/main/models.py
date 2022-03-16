from django.db import models
from PIL import Image
class Room(models.Model):

    name = models.CharField(unique=True, max_length=40)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='photos/')
    exist = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image:
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)
            if img.height > 100 or img.width > 100:
                middle = min(img.height, img.width)
                new_img = img.crop(
                    ((img.width - middle) // 2,
                     (img.height - middle) // 2,
                     img.width - (img.width - middle) // 2,
                     img.height - (img.height - middle) // 2))
                new_img = new_img.resize((100, 100))
                new_img.save(self.image.path)


class Interior(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    exist = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name + ' | ' + self.room.name


class Displacement(models.Model):

    object = models.ForeignKey(to=Interior, on_delete=models.CASCADE)
    from_room = models.ForeignKey(to=Room, null=True, related_name='from_room', on_delete=models.CASCADE)
    to_room = models.ForeignKey(to=Room, null=True, related_name='to_room', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.object.name + ' | ' + self.from_room.name + ' | ' + self.to_room.name + ' | ' + str(self.date)

