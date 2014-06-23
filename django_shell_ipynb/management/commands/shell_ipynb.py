from django.core.management.base import NoArgsCommand
import os
import sys

class Command(NoArgsCommand):

    help = "Runs a Python interactive interpreter using the IPython notebook."
    requires_model_validation = False

    def ipython_notebook(self):
        # analogous to the calls in the django.core shell command
        from IPython.html.notebookapp import NotebookApp

        app = NotebookApp.instance()
        # send it empty argv (default is None), else it picks up django manage
        # params and exits with a "no such file or directory" error
        app.initialize(argv=[])
        app.start()

    def handle_noargs(self, **options):
        # workaround taken from django.core.management.commands.shell
        # XXX: (Temporary) workaround for ticket #1796: force early loading of all
        # models from installed apps.
        from django.db.models.loading import get_models
        get_models()

        self.ipython_notebook()



