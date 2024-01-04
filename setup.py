from setuptools import find_packages, setup

__version__ = "20240104.0"
__author__ = "Dax Mickelson"
__author_email__ = "fmp@daxm.net"
__license__ = "BSD"
__package_name__ = "fmpsdk"
__description__ = "SDK for interacting with FMP's APIs."
__long_description__ = """Interact with Financial Modeling Prep's APIs."""
__url__ = "https://github.com/daxm/fmpsdk"

setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    keywords="fmpsdk financial stock valuation",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=["python-dotenv", "requests"],
    python_requires=">=3.6",
    package_data={},
    data_files=[],
)
