# Generated by Django 4.2.5 on 2023-09-26 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lc', '0002_category_users_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.RenameField(
            model_name='users',
            old_name='is_publisher',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='users',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lc.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='users',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='users',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
