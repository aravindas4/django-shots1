# Generated by Django 3.1.6 on 2021-02-13 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, default=5, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=5)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.blog')),
            ],
        ),
    ]
