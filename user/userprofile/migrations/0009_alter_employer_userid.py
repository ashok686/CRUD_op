# Generated by Django 3.2.14 on 2022-07-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_employer_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='userId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.user'),
        ),
    ]
