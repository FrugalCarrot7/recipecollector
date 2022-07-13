# Generated by Django 4.0.6 on 2022-07-13 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='step',
            name='step',
            field=models.IntegerField(verbose_name='add the step number'),
        ),
    ]
