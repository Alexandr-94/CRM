# Generated by Django 4.0.2 on 2022-02-17 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='languages',
            field=models.ForeignKey(blank=True, choices=[('LOW', 'Слабый'), ('MIDDLE', 'Средний'), ('HIGHER', 'Высокий')], help_text='Выберите язык которым владеети', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.languages', verbose_name='Язык'),
        ),
    ]
