# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

setup(
    name='abantether',
    version='0.0.1',
    author='Abantether',
    author_email='info@abantether.com',
    description='Abantether connector python sdk help you connect api',
    long_description_content_type="text/markdown",
    url='https://github.com/xibalbas/abantether-connector-python',
    project_urls={
        "Bug Tracker": "https://github.com/xibalbas/abantether-connector-python/issues"
    },
    license='commercial',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'requests',
    ],
    python_requires='>=3.8'
)
