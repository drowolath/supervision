.. _supervision_configuration:

Configuring supervision
=======================

supervision is expecting sections grouping informations regarding:

* cameras from which it'll grab snapshots
* databases in which it'll store gps tracks
* plugins from which it'll get custom code

Informations needed
-------------------

Cameras
*******

The essential infos for supervision regarding cameras is a way to identify them,
and access their http interface (for now this is the only way envisionned).
So, for a section named camera_x it'll expect the following mandatory options :

* name: a name identifying the camera
* url: the HTTP path to getting an instant snapshot
* username: the username to access the url, if needed
* password: the password to access the url, if needed
* snapshots_folder: the absolute path on disk where snapshots will be stored

Database storage
****************

If you need to store into a database, supervision uses the awesome `Records <http://github.com/kennethreitz/records.git`_ interface to talk to any database engine you may have.

It only awaits for sections named database_x and will look for the following mandatory options:

* engine: the actual DB engine (mysql, postgres, sqlite, oracle, ...)
* dbname: the database name
* host: fqdn or ip address of the host on which the DB engine is
* password: password to access the database, if needed    
* username: username to access the database, if needed
    

Plugins
*******

One mandatory plugin for supervisor is the code for parsing GPS tracks.
It will look for a section named 'plugins' in the configuration file.
Under this section, it will look for a mandatory option:

* folder: the folder in which you have stored your :file:`supervision_plugins/` directory
* .py file name: no value assigned to this option; its only name is enough

Example:

.. code-block:: bash

   [plugins]
   folder=/path/to/location
   gpsparser

   
Configuration commands
----------------------

supervision provides a CLI interface to simply configure it.

Adding/editing a camera
***********************

.. code-block:: bash

   $ supervision camera <name> --config

It will prompt for vital informations and create/modify cameras.

Adding/editing a database
*************************

.. code-block:: bash

   $ supervision database <name> --config

It will prompt for vital informations and create/modify databases.
