happycoding
===========

Development Setup
-----------------

.. code-block:: bash

    pyvenv venv
    source venv/bin/activate # or venv/Scripts/activate (on windows)
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
