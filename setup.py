from setuptools import setup, find_packages


setup(
    name='corgiweb',
    version='0.1',
    license='MIT',
    author="Jose Enriquez",
    author_email='joseaenriqueza@hotmail.com',
    packages=find_packages('corgiweb'),
    package_dir={'': 'corgiweb'},
    url='https://dev.azure.com/joseaenriqueza/_git/groupcrawler',
    keywords='Demo with testing, send email to get access to repo',
    install_requires=[
          'pytest',
      ],

)
