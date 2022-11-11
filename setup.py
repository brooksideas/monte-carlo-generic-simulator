import setuptools

with open("README.md") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="mcgs",  # This is the name of the package
    version="0.0.2",  # The release version
    author="Brook Tarekegn Assefa",  # Full name of the author
    author_email="brooksideas@gmail.com",
    description="A Simple Monte Carlo Simulator for different board games such as Coin flips , Dice rolls , "
                "Roman Alphabet , Card shuffle and many more",
    long_description=readme,  # Long description read from the readme file
    long_description_content_type="text/markdown",
    keywords="python, monte,carlo, generic, simulator, monte-carlo, monte-carlo-generic, monte carlo generic "
             "simulator, dice, coin, flip, alphabet",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.6',  # Minimum version requirement of the package
    py_modules=["mcgs"],  # Name of the python package
    package_dir={'': ''},  # Directory of the source code of the package
    install_requires=[],  # Install other dependencies if any
    license="MIT license",
    data_files=[(".", ["LICENSE"])],
    url="https://github.com/brooksideas/monte-carlo-generic-simulator",
    Project_URL="Documentation, https://github.com/brooksideas/monte-carlo-generic-simulator/blob/main/README.md, "
                "Issues , https://github.com/brooksideas/monte-carlo-generic-simulator/issues ,  "
)
