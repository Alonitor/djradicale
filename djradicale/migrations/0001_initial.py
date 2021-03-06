# Generated by Django 2.0 on 2018-01-11 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True, verbose_name='Path')),
                ('parent_path', models.TextField(verbose_name='Parent Path')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'db_table': 'djradicale_collection',
            },
        ),
        migrations.CreateModel(
            name='DBItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Text')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='djradicale.DBCollection', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'djradicale_item',
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='DBProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True, verbose_name='Path')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Properties',
                'verbose_name_plural': 'Properties',
                'db_table': 'djradicale_properties',
            },
        ),
        migrations.AlterUniqueTogether(
            name='dbitem',
            unique_together={('name', 'collection')},
        ),
    ]
