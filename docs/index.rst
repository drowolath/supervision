.. _supervision:

supervision
===========

Have you ever considered pluging in one project all of your personal cameras data?

That's what supervision is about: having a shedulers manager to collect all your private data from your IP cameras.
Focus is put on the simplicity of use and pure REST API.

Requirements
------------

* rabbitmq-server 3.3
* python2.7
* celery 3.1
* Flask 0.10
* PIL 2.6
* requests 2.4

Installation
------------

.. code-block:: bash

   $ git clone http://github.com/drowolath/supervision.git
   $ cd supervision
   /supervision# python setup.py install

By now, supervision will be in your PYTHON PATH and importable.

Configuration
-------------

.. note:: See :ref:`supervision_configuration` for more details

supervision will need configuration to be able to fetch data and organize them.
This configuration will be found in an INI file located at /etc/supervision/supervision.ini

Usage
-----

.. note:: See :ref:`supervision_management` for more details

You should consider using supervisord to manage the Celery schedulers provided by supervision.

