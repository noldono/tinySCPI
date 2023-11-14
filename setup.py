from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '1.0.1'
DESCRIPTION = 'An interface that enables the use of SCPI commands for the tinySA'
LONG_DESCRIPTION = ''

# Setting up
setup(
    name="tinyscpi",
    version=VERSION,
    author="tinySCPI Team",
    author_email="<rndonovan1@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pillow', 'wheel', 'setuptools', 'pyserial'],
    keywords=['python', 'scpi', 'interface', 'commands'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)