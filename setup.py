""" StationXML Utils
See:
https://github.com/flyrok/StationXML_utils
"""

from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent

# Get the long description from the README file
readme=here / 'README.md'
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

PROJECT_NAME="StationXML_utils"
#exec(open(here / "StationXML_utils/version.py").read())

VERSION=0.01
DESCRIPTION="Utilities for StationXML files"
URL="https://github.com/flyrok/StationXML_util"
AUTHOR="A Ferris"
EMAIL="aferris@flyrok.org"
CLASSIFIERS=['Development Status :: 3 - Alpha',
    'Intended Audience :: Seismic Researchers',
    'Topic :: Obspy/FDSN :: Helper Scripts',
    'License :: OSI Approved :: GPL-3 License',
     'Programming Language :: Python :: 3']
KEYWORDS="seismology obspy earthquakes response"     

setup(
    name=PROJECT_NAME,  # Required
    version=VERSION,  # Required
    description=DESCRIPTION,  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url=URL,  # Optional
    author=AUTHOR,  # Optional
    author_email=EMAIL,  # Optional
    classifiers=CLASSIFIERS ,
    keywords=KEYWORDS,  # Optional
    python_requires='>=3.6',
    include_package_data=True,
    packages=['stationxml_utils'],
    entry_points={  # Optional
        'console_scripts': [
            'staxml_respinfo=stationxml_utils.staxml_respinfo:main',
            'make_NRL_inv=stationxml_utils.make_NRL_inv:main',
            'dataless2inv=stationxml_utils.dataless2inv:main',
            'plot_staxml=stationxml_utils.plot_staxml:main',
        ],
    },
    extras_require={  # Optional
    },
    package_data={  
    },
    project_urls={  # Optional
        'Source': URL,
    },
)

