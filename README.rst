Django Shell IPython Notebook
=============================

This Django app adds one shell command, ``shell_ipynb``, which starts up
the IPython Notebook as your Django shell instead of the default. The
IPython Notebook has several advantages, including that you can save a
whole experimentation session as a reusable notebook, and HTML-based
completion and code documentation.

After having installed ``django-shell-ipynb`` with ``pip`` or manually,
add it to your Django project's ``INSTALLED_APPS``.

After having done this, you can start up the IPython Notebook Django
shell with::

    python manage shell_ipynb


