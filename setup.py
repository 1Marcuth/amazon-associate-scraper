from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme_content = file.read()

setup(
    name="amazon-affiliate-scraper",
    version="1.24.2",
    license="MIT License",
    author="Marcuth",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author_email="marcuth2006@gmail.com",
    keywords="amazon affiliate scraper",
    description=f"Utilities and tools for things related to Dragon City",
    packages=["amazon_affiliate"] + [ "amazon_affiliate/" + x for x in find_packages("amazon_affiliate") ]
)