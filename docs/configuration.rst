.. _supervision_configuration:

Configuring supervision
=======================

supervision is expecting sections grouping informations regarding:

* cameras from which it'll grab snapshots


Informations needed
-------------------


The essential infos for supervision regarding cameras is a way to identify them,
and access their http interface (for now this is the only way envisionned).
So, for a section named camera_x it'll expect the following mandatory options :

* name: a name identifying the camera
* url: the HTTP path to getting an instant snapshot
* username: the username to access the url, if needed
* password: the password to access the url, if needed
* snapshots_folder: the absolute path on disk where snapshots will be stored

   
Configuration commands
----------------------

supervision provides a CLI interface to simply configure it.

.. code-block:: bash

   $ supervision camera <name> --config

It will prompt for vital informations and create/modify cameras.
