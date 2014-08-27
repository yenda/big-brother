.. _install_development:

=======================
Development environment
=======================

Quick start
===========

.. note:: If you have some global utilities (like buildout, ipython, etc.) 
   installed, you could pass the option ``--system-site-packages`` to the
   ``virtualenv`` command.

#. Navigate to the location where you want to place your project.

#. Get the code::

    $ hg clone ssh://hg@bitbucket.org/maykinmedia/bigbrother
    $ cd bigbrother

#. Bootstrap the virtual environment and install all required libraries. The
   ``boostrap.py`` script basically sets the proper Django settings file to be
   used::

    $ python bootstrap.py <production|staging|test|development>

#. Activate your virtual environment and create the statics and database::

    $ source env/bin/activate
    $ cd src
    $ python manage.py collectstatic --link
    $ python manage.py syncdb --migrate


Next steps
----------

Optionally, you can load demo data and extract demo media files::

    $ python manage.py loaddata demo
    $ cd ../media
    $ tar -xzf demo.tgz

You can now run your installation and point your browser to the address given
by this command::

    $ python manage.py runserver
