# Generated by Django 3.2.14 on 2022-07-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('isAdmin', models.BooleanField()),
            ],
        ),
    ]
