"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass