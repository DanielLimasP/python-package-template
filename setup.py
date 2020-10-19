import setuptools

with open("README.md", "r") as file_header:
    long_description = file_header.read()

setuptools.setup(
    name="new-template-USERNAME",
    version="",
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires='>=3.6',
)