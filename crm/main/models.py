from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=40,
                            help_text="Введите название компании",
                            verbose_name="Название компании")
    description = models.TextField(max_length=300,
                                   help_text="Введите краткое описание компании",
                                   verbose_name="Описание компании")
    country = CountryField(help_text="Выберите страну",
                           verbose_name="Страна регистрации компании")
    address = models.CharField(max_length=100,
                               help_text="Введите полный адрес расположения компании",
                               verbose_name="Адрес компании")
    people = models.ManyToManyField('People',
                               help_text="Выберите работников",
                               verbose_name="Работники")

    def __str__(self):
        return self.name


class People(models.Model):
    LEVEL = (
        ('LOW', 'Слабый'),
        ('MIDDLE', 'Средний'),
        ('HIGHER', 'Высокий'),
    )

    first_name = models.CharField(max_length=30,
                                  help_text="Введите имя",
                                  verbose_name="Имя")
    patronymic = models.CharField(max_length=40,
                                  help_text="Введите отчество",
                                  verbose_name="Отчество")
    last_name = models.CharField(max_length=30,
                                 help_text="Введите фамилию",
                                 verbose_name="Фамилия")
    date_of_birth = models.DateField(help_text="Введите дату рождения",
                                     verbose_name="Дата рождения",
                                     null=True, blank=True)

    languages = models.ForeignKey('Languages', on_delete=models.CASCADE,
                                       help_text="Выберите язык которым владеети",
                                       verbose_name="Язык", null=True
                                  )
    level = models.CharField(max_length=6, choices=LEVEL, blank=True,
                             help_text="Выберите уровень знания языка",
                             verbose_name="Уровень")

    skills = models.CharField(max_length=200,
                              help_text="Введите свои навыки",
                              verbose_name="Навыки")

    def __str__(self):
        return self.last_name


class Languages(models.Model):

    languages = models.CharField(max_length=20,
                                 help_text="Введите язык",
                                 verbose_name="Язык")

    def __str__(self):
        return self.languages