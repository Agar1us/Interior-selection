# Generated by Django 4.0.3 on 2022-03-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Название комнаты')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m', verbose_name='Фоторафия комнаты')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Interiors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Предмет')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.rooms', verbose_name='Расположение')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентарь',
            },
        ),
        migrations.CreateModel(
            name='Displacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время перемещения')),
                ('last_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.rooms', verbose_name='Прошлое расположение')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.interiors', verbose_name='Инвентарь')),
            ],
            options={
                'verbose_name': 'Перемещение объекта',
                'verbose_name_plural': 'Перемещение объекта',
            },
        ),
    ]
