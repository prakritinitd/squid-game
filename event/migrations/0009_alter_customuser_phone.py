# Generated by Django 4.0 on 2022-01-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_remove_round2_cheater_remove_round2_gameover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
