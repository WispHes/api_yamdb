from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import validate_year
from user.models import User


class BaseModel(models.Model):

    name = models.CharField(max_length=300, verbose_name='Наименование')
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Genre(BaseModel):

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Category(BaseModel):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    year = models.PositiveSmallIntegerField(
        verbose_name='Дата выхода',
        validators=[validate_year]
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']


class ReviewAndCommentBasicModel(models.Model):
    text = models.CharField(
        max_length=1000,
        verbose_name='Текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return self.text

    class Meta:
        abstract = True


class Review(ReviewAndCommentBasicModel):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author', ),
                name='unique review'
            )]
        ordering = ('pub_date',)


class Comment(ReviewAndCommentBasicModel):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )

    class Meta:
        ordering = ('review', 'author')
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'
