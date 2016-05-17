.. _supervision_management:

Managing supervision
====================

supervision proposes Celery apps to manage periodic and repetitive tasks.
For now, it has two apps:

* gpsparser: a GPS tracks parser; you may plug a custom one in configuration
* cameras: a crawler that will periodically fetch snapshots from cameras configured

Launching celery apps
---------------------

.. note:: See `http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#running-the-celery-worker-server`_ for more infos

If you've ever used Celery, it's really straightforward:

.. code-block:: bash

   $ celery worker -n gpsparser@locahlost -A supervision.gpsparser -Q dispatch,parse,record
   $ celery worker -n cameras@localhost -A supervision.cameras --beat --schedule /var/lib/celery/ipcam_beat.db -Q download,purge

The "-Q" option in Celery gives precision on which Queue to implement.
The "--beat" tells celery to run the periodic tasks scheduler too.

You can also use Supervisord to manage the apps.
See `https://github.com/celery/celery/blob/3.1/extra/supervisord/`_ for a beautiful example of how to use it.
