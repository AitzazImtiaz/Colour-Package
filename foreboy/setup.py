from setuptools import setup

setup(
    name = "foreboy",
    version = "1.0.0",
    description = "Change text colour",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Colour-Package",
    packages = ["foreboy"],
    entry_points = {
        'console_scripts': [
            'foreboy = foreboy.__main__:main'
        ]
    },
)
