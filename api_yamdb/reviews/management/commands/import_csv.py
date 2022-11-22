import csv

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

FILES = {
    'Category': 'category.csv',
    'Genre': 'genre.csv',
    'Title': 'titles.csv',
    'GenreTitle': 'genre_title.csv',
    'User': 'users.csv',
    # 'Review': 'review.csv',
    # 'Comment': 'comments.csv'
}


class Command(BaseCommand):
    help = 'adds data from csv files to the database'

    def handle(self, *args, **options):
        for model_name, file_name in FILES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file_name}',
                encoding='utf-8-sig'
            ) as csv_file:
                file_reader = csv.DictReader(csv_file, delimiter=',')
                model = apps.get_model(
                    app_label='reviews',
                    model_name=model_name
                )
                for row in file_reader:
                    model.objects.get_or_create(**row)
