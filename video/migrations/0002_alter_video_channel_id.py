# Generated by Django 4.0.5 on 2023-07-12 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel'),
        ),
    ]
