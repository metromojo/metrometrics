
from setuptools import setup

setup(
        name = 'metrometrics',
        version = '0.1',
        description= 'GIS tool for predicting battery degradation'
            'in public transit busses',
        author='Ryan Carlin, Erica Eggleton, Harrison Goldwyn',
        author_email='carlin31@uw.edu',
        url='https://github.com/metromojo/metrometrics',
        packages=['metrometrics'],
        package_dir={"project" : 'metrometrics'}
        )
