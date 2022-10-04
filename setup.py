from os import path

import setuptools

HERE = path.dirname(path.abspath(__file__))


with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as file:
    all_reqs = file.read().split('\n')

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="cloudphoto",
    version="0.1",
    author="Anvar",
    author_email="anvar00755@mail.ru",
    description="This is a homework.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Badmoon-mySun/cloudphoto",
    packages=setuptools.find_packages("src"),
    include_package_data=True,
    package_dir={"": "src"},
    install_requires=all_reqs,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: KFU License"
    ],
    entry_points={
        'console_scripts': [
            'cloudphoto = cloudphoto.cloudphoto:main',
        ],
    },
    python_requires='>=3.5',
)