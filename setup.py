from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gh-pages-test',
    version='0.1.2',
    license='GNU General Public License v3.0',
    description='p-Adic numbers and finite fields in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Giuseppe De Laurentis',
    author_email='g.dl@hotmail.it',
    url='https://github.com/GDeLaurentis/gh-pages-test',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'sympy'],
)
