from setuptools import setup, find_packages

setup(
    name='django-shell-ipynb',
    version='0.1.0',
    description='A management command "shell_ipynb" that uses the ipython notebook instead of ipython.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Charl P. Botha',
    author_email='cpbotha@vxlabs.com',
    url='https://github.com/cpbotha/django-shell-ipynb',
    download_url='https://github.com/cpbotha/django-shell-ipynb/downloads',
    license='BSD',
    packages=['django_shell_ipynb'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
