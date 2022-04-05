from setuptools import find_packages, setup

__author__ = "Dax Mickelson"
__author_email = "fmp@daxm.net"
__license__ = "BSD"

setup(
    name="fmpsdk",
    version="20220405.0",
    description="SDK for interacting with FMP's APIs.",
    long_description="""Interact with Financial Modeling Prep's APIs.""",
    url="https://github.com/daxm/fmpsdk",
    author="Dax Mickelson",
    author_email="fmp@daxm.net",
    license="BSD",
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
    data_files=None,
)
