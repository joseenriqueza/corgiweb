

Example Project
===============
This is an example project that is used to demonstrate how to publish
Python packages on PyPI. To take a look at the step by step guide on how to 
do so, make sure you read `the article on Towards Data Science <https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3>`_.

I did some modifications to use pandas as the testing library

Installing
============

.. code-block:: bash

    pip install groupcrawler

Usage
=====

.. code-block:: bash

    >>> from src.example import groupcrawler
    >>> groupcrawler.get_pandas_version()
    '0.24.2'
