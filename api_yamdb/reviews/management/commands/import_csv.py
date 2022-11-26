import csv

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment
from user.models import User

FILES = [
    (User, 'users.csv'),
    (Category, 'category.csv'),
    (Genre, 'genre.csv'),
    (Title, 'titles.csv'),
    (apps.get_model(app_label='reviews', model_name='title_genre'),
        'genre_title.csv'),
    (Review, 'review.csv'),
    (Comment, 'comments.csv'),
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
        if options['users']:
            files.append((User, 'users.csv'))
            load_all = False
        if options['category']:
            files.append((Category, 'category.csv'))
            load_all = False
        if options['genre']:
            files.append((Genre, 'genre.csv'))
            load_all = False
        if options['titles']:
            files.append((Title, 'titles.csv'))
            load_all = False
        if options['genre_title']:
            files.append(
                (apps.get_model(app_label='reviews', model_name='title_genre'),
            'genre_title.csv'))
            load_all = False
        if options['review']:
            files.append((Review, 'review.csv'))
            load_all = False
        if options['comments']:
            files.append((Comment, 'comments.csv'))
            load_all = False
        if load_all == True:
            files = FILES
        print(files)
        for model, file_name in files:
            try:
                with open(
                    f'{settings.BASE_DIR}/static/data/{file_name}',
                    encoding='utf-8-sig'
                ) as csv_file:
                    file_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in file_reader:
                        model.objects.get_or_create(**row)
            except IOError:
                print('Could not read file:', file_name)
