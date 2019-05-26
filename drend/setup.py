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
    ],
    license='MIT',
    keywords=[
        'python',
        'django',
    ],
)
