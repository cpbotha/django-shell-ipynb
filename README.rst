Django Shell IPython Notebook
=============================

This Django app adds one shell command, ``shell_ipynb``, which starts up
the IPython Notebook as your Django shell instead of the default. The
IPython Notebook has several advantages, including that you can save a
whole experimentation session as a reusable notebook, and HTML-based
completion and code documentation.

Installation
------------
After having installed ``django-shell-ipynb`` with ``pip`` (from github
or from pypi) or manually, add it to your Django project's ``INSTALLED_APPS``.  

After having done this, you can start up the IPython Notebook Django
shell with::

    python manage shell_ipynb

Alternatives
------------
You can get the same behaviour by installing and using the
`django-extensions
<https://github.com/django-extensions/django-extensions>`_ app, which  
comes with a whole bunch of other management commands you might want or
not want.
