import importlib
import fastentrypoints
from setuptools import setup, find_packages

# don't execute __init__.py to get the data
spec = importlib.util.spec_from_file_location('__data__', './cognito_login/__data__.py')
package_data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_data)

setup(
    name=package_data.NAME,
    packages=find_packages(exclude=['tests/*']),
    version=package_data.VERSION,
    author=package_data.AUTHOR,
    author_email=package_data.AUTHOR_EMAIL,
    description=package_data.DESCRIPTION,
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license=package_data.LICENSE,
    url=package_data.HOMEPAGE,
    install_requires=[
        'pluggy',
        'warrant',
        'configargparse',
        'python-jose[pycryptodome]~=3.1.0',
    ],
    entry_points={
        'console_scripts': [
            'cognito-login=cognito_login.cli.main:main',
        ],
    },
    python_requires='>=3.5',
)
