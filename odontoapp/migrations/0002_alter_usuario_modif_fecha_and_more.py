# Generated by Django 4.1.1 on 2022-10-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odontoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='modif_fecha',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='modif_usuario',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
