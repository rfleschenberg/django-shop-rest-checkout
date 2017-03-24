========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/django-shop-rest-checkout/badge/?style=flat
    :target: https://readthedocs.org/projects/django-shop-rest-checkout
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/rfleschenberg/django-shop-rest-checkout.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/rfleschenberg/django-shop-rest-checkout

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/rfleschenberg/django-shop-rest-checkout?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/rfleschenberg/django-shop-rest-checkout

.. |requires| image:: https://requires.io/github/rfleschenberg/django-shop-rest-checkout/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/rfleschenberg/django-shop-rest-checkout/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/rfleschenberg/django-shop-rest-checkout/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/rfleschenberg/django-shop-rest-checkout

.. |version| image:: https://img.shields.io/pypi/v/django-shop-rest-checkout.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-shop-rest-checkout

.. |commits-since| image:: https://img.shields.io/github/commits-since/rfleschenberg/django-shop-rest-checkout/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/rfleschenberg/django-shop-rest-checkout/compare/v0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/django-shop-rest-checkout.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-shop-rest-checkout

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-shop-rest-checkout.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-shop-rest-checkout

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-shop-rest-checkout.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-shop-rest-checkout

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-shop-rest-checkout.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-shop-rest-checkout


.. end-badges

ReST-based checkout for django-shop

* Free software: BSD license

Installation
============

::

    pip install django-shop-rest-checkout

Documentation
=============

https://django-shop-rest-checkout.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
