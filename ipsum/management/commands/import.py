from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Import phrases that we started earlier
    They're in a return-delimited text file
    """
    def handle(self, *args, **kwargs):
        import os
        from ipsum.models import Phrase

        this_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(this_path, 'edisums.txt')

        with open(path, 'r') as f:
            phrases = f.readlines()

        for phrase in phrases:
            phrase = Phrase.objects.create(
                phrase=phrase.strip('\n'),
                approved=True
            )
            print phrase
