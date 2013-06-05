Django Shell IPython Notebook
=============================

This Django app adds one shell command, ``shell_ipynb``, which starts up
the IPython Notebook as your Django shell instead of the default. The
IPython Notebook has several advantages, including that you can save a
whole experimentation session as a reusable notebook, and HTML-based
completion and code documentation.

Installation
------------
The easiest way to install ``django-shell-ipynb`` is to use ``pip``.
Either do this from pypi::

    pip install django-shell-ipynb

Or directly from github::

    pip install git+git://github.com/cpbotha/django-shell-ipynb.git 

After successful installation, add ``django_shell_ipynb`` to your Django
project's ``INSTALLED_APPS``.  

After having done this, you can start up the IPython Notebook Django
shell with::

    python manage.py shell_ipynb

At which point your browser should start up with the IPython Dashboard,
from which you can create new or edit existing notebooks.

Alternatives
------------
You can get the same behaviour with the ``shell_plus`` management
command added by `django-extensions
<https://github.com/django-extensions/django-extensions>`_ app, which  
comes with a whole bunch of other management commands you might want or
not want.

After releasing 0.2.0, I also discovered `django_ipython_notebook
<https://github.com/bentoner/django_ipython_notebook>`_. However, that
one internally uses the deprecated
``django.core.management.setup_environ()`` function hardcoded for
``settings``, and executes ipython using ``os.system()``, both of which
are not ideal.
