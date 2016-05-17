# supervision (or else)

Have you ever considered pluging in one project all of your personal tracking data?
May it be cameras at home or the backhauling of GPS data, having them managed by one tiny app?

That's what supervision is about: having a shedulers manager to collect all your private data.
Focus is put on the simplicity of use and pure REST API.

## What's needed?

* RabbitMQ 3.3
* python2.7
* celery 3.1
* Flask 0.10
* PIL 2.6
* records 0.4
* requests 2.4

## How to install?

```bash
$ git clone http://github.com/drowolath/supervision.git
$ cd supervision
/supervision# python setup.py install
```

By now, supervision will be in your PYTHON PATH and importable.

## How to configure?

supervision will need configuration to be able to fetch data and organize them.
This configuration will be found in an INI file located at /etc/supervision/supervision.ini
See docs/configuration.rst for more details

## How to use?

You should consider using supervisord to manage the Celery schedulers provided by supervision.
You will find an example in docs/management.rst
