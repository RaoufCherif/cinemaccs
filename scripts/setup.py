from setuptools import find_packages, setup

setup(
    name="scrapping",
    packages=find_packages(exclude=["scrapping_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
