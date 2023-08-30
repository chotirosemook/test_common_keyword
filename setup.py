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

extra_math = [
    'returns-decorator',
]
extra_bin = [
    *extra_math,
]
extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='AscendQaCommonLibrary',
    version=VERSION,
    description='Ascend qa common library',
    author='Ascend Commerce',
    author_email='your@email.com',
    url = 'https://gitlab.weomni.com/ascend-commerce/qa1/ascend-qa-common-keywords.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires= REQUIREMENTS
)