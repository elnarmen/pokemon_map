from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    title_en = models.CharField(max_length=50, verbose_name='Английское имя')
    title_jp = models.CharField(max_length=50, verbose_name='Японское имя')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, verbose_name='Изображение')
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='next_evolutions',
        verbose_name='Из кого эволюционировал'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Дата и время появления')
    disappeared_at = models.DateTimeField(verbose_name='Дата и время изчезновения')
    level = models.IntegerField(default=1, verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(default=100, verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(default=100, verbose_name='Атака', null=True, blank=True)
    defence = models.IntegerField(default=100, verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(default=100, verbose_name='Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon}-{self.pk}'