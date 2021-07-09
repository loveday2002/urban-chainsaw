# Ensures that we can install a package with pip install package

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='urban-chainsaw',
    version='0.0.3',
    author='loveday2002',
    author_email='loveday2002@gmail.com',

    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/loveday2002/urban-chainsaw',
    project_urls = {
        "Bug Tracker": "https://github.com/loveday2002/urban-chainsaw/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
