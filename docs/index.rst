.. Connexions Database Library documentation master file, created by
   sphinx-quickstart on Tue Mar 22 15:31:49 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Connexions Database Library
===========================

.. image:: https://travis-ci.org/Connexions/cnx-db.svg
   :target: https://travis-ci.org/Connexions/cnx-db

.. image:: https://coveralls.io/repos/Connexions/cnx-db/badge.png?branch=master
   :target: https://coveralls.io/r/Connexions/cnx-db?branch=master

.. image:: https://badge.fury.io/py/cnx-db.svg
   :target: http://badge.fury.io/py/cnx-db

Contents:

.. toctree::
   :maxdepth: 2

Installation
------------

Install using one of the following methods (run within the project root)::

    python setup.py install

Or::

    pip install .

Usage
-----

Initialize an database::

    cnx-db init <app-config>.ini

Replace ``<app-config>.ini`` with the application configuration file.

.. todo:: This may become part of ``dbmigrator init`` or ``dbmigrator migrate``
          in the future.

Testing
-------

The tests require access to a blank database named ``cnxarchive-testing``
with the user ``cnxarchive`` and password ``cnxarchive``. This can easily
be created using the following commands::

    psql -c "CREATE USER cnxarchive WITH SUPERUSER PASSWORD 'cnxarchive';"
    createdb -O cnxarchive cnxarchive-testing

The tests can then be run using::

    python setup.py test

License
-------

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2013 Rice University


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

