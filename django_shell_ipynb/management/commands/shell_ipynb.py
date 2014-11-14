""" iPython Notebook management command. """

from django.core.management.base import BaseCommand

import os
import sys


class Command(BaseCommand):

    """ iPython notebook command. """

    help = "Runs a Python interactive interpreter using the IPython notebook."
    requires_model_validation = False

    def run_from_argv(self, argv):
        """ Store ARGV before running. """
        self._argv = argv
        self.execute()

    def ipython_notebook(self):
        """ Create the notebook app, after having patched PYTHONPATH. """

        # If manage.py modified sys.path, we need that, because of
        # https://github.com/ipython/ipython/issues/5420#issuecomment-38503775
        os.environ['PYTHONPATH'] = ':'.join(sys.path)

        # analogous to the calls in the django.core shell command
        from IPython.html.notebookapp import NotebookApp

        app = NotebookApp.instance()

        app.initialize(argv=self._argv[1:])
        app.start()

    def handle(self, *args, **options):
        """ Handle the Django management command. """

        from django.db.models.loading import get_models
        get_models()

        self.ipython_notebook()
