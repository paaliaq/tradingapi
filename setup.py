"""Setup for the tradingapplication package."""

from setuptools import find_packages, setup

setup(
    name="tradingapi",
    packages=find_packages("src/"),
    version="0.1.0",
    description="This repo defines define the connection to the core trading apis.",
    author="August Andersen",
    license="",
    python_requires=">=3.8"
)
