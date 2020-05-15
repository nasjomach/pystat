import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystat-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Jonas Macheret",
    author_email="macheretj@gmail.com",
    description="PyStat system performance collector and grapher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)