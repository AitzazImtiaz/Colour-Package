from setuptools import setup

setup(
    name = "backboy",
    version = "1.0.0",
    description = "Change terminal colour",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Colour-Package",
    packages = ["backboy"],
    entry_points = {
        'console_scripts': [
            'backboy = backboy.__main__:main'
        ]
    },
)
