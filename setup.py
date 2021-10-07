from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="flask_clean_code",
    version="0.0.1",
    packages=find_packages(),
    author="Vinicius Gazolla Boneto",
    author_email="vineboneto@gmail.com",
    url="http://github.com/vineboneto/flask_clean_code",
    include_package_data=True,
    long_description=open("readme.md").read(),
    install_requires=required,
)
