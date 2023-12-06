import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="portfolio",
    version="0.01",
    description="Python objects to contain generic market info, to be used in trading systems with any broker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vankovp/portfolio",
    packages=setuptools.find_packages(),
    python_requires=">=3.11",
    install_requires=[
    ],
)
