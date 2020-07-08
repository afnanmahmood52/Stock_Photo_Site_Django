# Generated by Django 3.0.6 on 2020-06-12 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(max_length=2000)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field='height', upload_to='images/', width_field='width')),
                ('category_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
                ('upload_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]