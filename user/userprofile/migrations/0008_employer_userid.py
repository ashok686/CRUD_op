# Generated by Django 3.2.14 on 2022-07-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='userId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
