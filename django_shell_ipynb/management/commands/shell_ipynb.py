
from django.core.management.base import BaseCommand

import os
import sys

class Command(BaseCommand):

    help = "Runs a Python interactive interpreter using the IPython notebook."
    requires_model_validation = False

    def run_from_argv(self, argv):
        self._argv = argv
        self.execute()

    def ipython_notebook(self):
        # analogous to the calls in the django.core shell command
        from IPython.html.notebookapp import NotebookApp

        app = NotebookApp.instance()

        app.initialize(argv=self._argv[1:])
        app.start()

    def handle(self, *args, **options):
        from django.db.models.loading import get_models
        get_models()

        self.ipython_notebook()
