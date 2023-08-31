import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

VERSION = join(CURDIR, 'src', 'AscendQaCommonLibrary', 'version.py')
exec(compile(open(VERSION).read(), VERSION, 'exec'))
# with open(join(CURDIR, 'README.rst')) as f:
#     DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='AscendQaCommonLibrary',
    version=VERSION,
    description='Ascend qa common library',
    author='Ascend Commerce',
    url = 'https://gitlab.weomni.com/ascend-commerce/qa1/ascend-qa-common-keywords.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires= REQUIREMENTS
)