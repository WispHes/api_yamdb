import csv

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment
from user.models import User

FILES = [
    (User, 'users.csv', 'users'),
    (Category, 'category.csv', 'category'),
    (Genre, 'genre.csv', 'genre'),
    (Title, 'titles.csv', 'titles'),
    (apps.get_model(app_label='reviews', model_name='title_genre'),
        'genre_title.csv', 'genre_title'),
    (Review, 'review.csv', 'review'),
    (Comment, 'comments.csv', 'comments'),
]


class Command(BaseCommand):
    help = 'adds data from csv files to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--users',
            action='store_true',
            default=False,
            help='Load users.csv'
        )
        parser.add_argument(
            '-c',
            '--category',
            action='store_true',
            default=False,
            help='Load category.csv'
        )
        parser.add_argument(
            '-g',
            '--genre',
            action='store_true',
            default=False,
            help='Load genre.csv'
        )
        parser.add_argument(
            '-t',
            '--titles',
            action='store_true',
            default=False,
            help='Load titles.csv'
        )
        parser.add_argument(
            '-r',
            '--review',
            action='store_true',
            default=False,
            help='Load review.csv'
        )
        parser.add_argument(
            '-o',
            '--comments',
            action='store_true',
            default=False,
            help='Load comments.csv'
        )
        parser.add_argument(
            '-e',
            '--genre_title',
            action='store_true',
            default=False,
            help='Load genre_title.csv'
        )

    def handle(self, *args, **options):
        files = []
        load_all = True
        for model, file_name, option in FILES:
            if options[option]:
                files.append((model, file_name, option))
                load_all = False
        if load_all is True:
            files = FILES
        self.stdout.write(self.style.SUCCESS(files))
        for model, file_name, option in files:
            try:
                with open(
                    f'{settings.BASE_DIR}/static/data/{file_name}',
                    encoding='utf-8-sig'
                ) as csv_file:
                    file_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in file_reader:
                        model.objects.get_or_create(**row)
            except IOError:
                self.stdout.write(
                    self.style.WARNING(f'Could not read file: {file_name}')
                )
