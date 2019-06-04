from distutils.core import setup

setup(
    name='Drend',
    version='1.0.0',
    description='Gathering my knowledge into practical tangible product',
    author='Meysam Azad',
    author_email='MeysamAzad81@yahoo.com',
    install_requires=[
        "Django==2.2.1",
        "gunicorn==19.9.0",
        'djangorestframework==3.9.4',
        'Markdown==3.1.1',
        'django-filter==2.1.0',
        'djongo==1.2.32',
        'sqlparse==0.2.4',
        'djangorestframework-jwt==1.11.0',
        'python-jose==3.0.1',
    ],
    license='MIT',
    keywords=[
        'python',
        'django',
    ],
)
