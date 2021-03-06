# Generated by Django 2.1.1 on 2018-09-18 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('weight', models.IntegerField(default=1)),
                ('introduction', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='')),
                ('img_info', models.CharField(blank=True, max_length=420)),
                ('img_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcxt.Dish')),
            ],
        ),
    ]
