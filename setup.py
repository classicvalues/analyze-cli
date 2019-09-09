import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel('intezer_analyze_cli', '__init__.py'), 'r') as f:
    version_marker = '__version__ = '
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip("'")
            break
    else:
        raise RuntimeError('Version marker not found.')

install_requires = [
    'requests==2.22.0',
    'click==6.7',
    'tenacity==5.0.3',
    'pyjwt==1.6.1',
    'intezer-sdk==0.14'
]
tests_require = [
    'pytest==3.1.2',
    'responses==0.10.6'
]

setup(
    name='intezer-analyze-cli',
    version=version,
    description='Client library for Intezer cloud service',
    author='Intezer Labs ltd.',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='intezer',
    packages=['intezer_analyze_cli'],
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points='''
        [console_scripts]
        intezer-analyze=intezer_analyze_cli.cli:main_cli
    ''',
    license='Apache License v2',
    python_requires='>=3.5',
    zip_safe=False
)
