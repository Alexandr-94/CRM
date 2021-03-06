# Generated by Django 4.0.2 on 2022-03-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_people_languages_people_languages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Country',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(help_text='Введите название компании', max_length=40, verbose_name='Название компании'),
        ),
        migrations.RemoveField(
            model_name='company',
            name='people',
        ),
        migrations.AddField(
            model_name='company',
            name='people',
            field=models.ManyToManyField(help_text='Выберите работников', to='main.People', verbose_name='Работники'),
        ),
    ]
