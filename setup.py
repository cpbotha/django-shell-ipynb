from setuptools import setup, find_packages

setup(
    name='django-shell-ipynb',
    version='0.3.0',
    description='A Django management command "shell_ipynb" that uses the ipython notebook instead of ipython.',
    long_description=open('README.rst').read(),
    author='Charl P. Botha',
    author_email='cpbotha@vxlabs.com',
    url='https://github.com/cpbotha/django-shell-ipynb',
    license='BSD',
    keywords = "django ipython notebook shell",
    # gets nested packages also, including
    # django_shell_ipynb.management.commands
    packages=find_packages(),
    # the ipython notebook requires tornado and pyzmq
    install_requires = ['ipython', 'tornado', 'pyzmq'],
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
