"""
Setup to package to pypi package
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
 
    name='imgdiff',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.0.0',  # Required

    description='A tool to compare similar images',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    author='Dheeraj As',  # Optional
    author_email='dheeraj.as008@gmail.com',  # Optional

    classifiers=[  # Optional
          # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='image similarity dhash',  # Optional
    py_modules=["imgdiff/diff"],
    # package_dir={'': 'imgdiff'},
    # package_dir={'mytest': 'src/mytest'},
    # packages=['imgdiff'],
    # Required
    python_requires='>=3.0, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['dhash','Pillow'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['pytest'],
        'test': ['pytest'],
    },
    project_urls={  # Optional
        'Source': 'https://github.com/RealNameHidden/img-diff',
    },
)