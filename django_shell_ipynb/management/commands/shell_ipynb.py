from django.core.management.base import NoArgsCommand
import sys


class Command(NoArgsCommand):

    help = "Runs a Python interactive interpreter using the IPython notebook."
    requires_model_validation = False

    def ipython_notebook(self):
        # analogous to the calls in the django.core shell command
        from IPython.frontend.html.notebook.notebookapp import NotebookApp
        app = NotebookApp.instance() 
        # except for this bit, we we pass sys.argv to the ipython
        # interpreter, so that it gets the location of manage.py,
        # inserting it into the PYTHONPATH and making it the default
        # notebook directory.
        app.initialize(argv=sys.argv) 
        app.start()

    def handle_noargs(self, **options):
        # workaround taken from django.core.management.commands.shell
        # XXX: (Temporary) workaround for ticket #1796: force early loading of all
        # models from installed apps.
        from django.db.models.loading import get_models
        get_models()

        self.ipython_notebook()



