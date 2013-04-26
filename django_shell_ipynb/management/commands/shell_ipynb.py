from django.core.management.base import NoArgsCommand
import os
import sys


class Command(NoArgsCommand):

    help = "Runs a Python interactive interpreter using the IPython notebook."
    requires_model_validation = False

    def ipython_notebook(self):
        # analogous to the calls in the django.core shell command
        from IPython.frontend.html.notebook.notebookapp import NotebookApp
        app = NotebookApp.instance()
        app.initialize()

        # here sys.path contains, as the first element, the directory containing
        # manage.py. However, in the kernels that are started for the actual
        # notebooks, sys.path does not contain this project directory. looks
        # like this has been fixed in IPython, and should be out AFTER 0.13.2:
        # https://github.com/ipython/ipython/commit/463ab6b388436efdb8bb2f949817e94c74f51dee

        # until that time, after 0.13.2 is released, we need the following
        # os.environ modification before and restoration after app.start()

        # get current PYTHONPATH
        pps = os.environ.get('PYTHONPATH')

        if pps is None:
            # remember that there was no PYTHONPATH to start with
            nopp = True
            pps = ''

        else:
            nopp = False

        # break up into components
        ppl = pps.split(os.pathsep)
        # path containing manage.py
        project_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        print project_path
        # add it
        ppl.append(project_path)
        # and set it
        os.environ['PYTHONPATH'] = os.pathsep.join(ppl)

        # start the notebook
        app.start()

        # user has quit the notebook, we restore the saved PYTHONPATH
        if nopp:
            # there was none to start with, so we delete it
            del os.environ['PYTHONPATH']

        else:
            os.environ['PYTHONPATH'] = pps

    def handle_noargs(self, **options):
        # workaround taken from django.core.management.commands.shell
        # XXX: (Temporary) workaround for ticket #1796: force early loading of all
        # models from installed apps.
        from django.db.models.loading import get_models
        get_models()

        self.ipython_notebook()



