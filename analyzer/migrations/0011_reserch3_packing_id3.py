# Generated by Django 4.0.7 on 2022-09-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0010_reserch1_send1_reserch2_send2_reserch3_send3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserch3',
            name='packing_id3',
            field=models.IntegerField(null=True),
        ),
    ]