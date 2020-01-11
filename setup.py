import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bplot-bparks", # Replace with your own username
    version="0.0.1",
    author="Ben Parks",
    author_email="bparks@stanford.edu",
    description="Plotting utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bnprks/bplot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)