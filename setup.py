"""Setup"""
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    description = (
        "An implementation of neural networks."
    ),
    name='projects',
    author = "Mahdi Ghiasi",
    author_email = "mahdiw.ghiasi@gmail.com",
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
)
