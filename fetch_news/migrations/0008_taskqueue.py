# Generated by Django 3.1.3 on 2020-11-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_news', '0007_auto_20201122_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulk_ref', models.CharField(max_length=50)),
                ('is_finished', models.BooleanField(db_index=True, default=False)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]