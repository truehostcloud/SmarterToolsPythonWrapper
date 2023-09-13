from setuptools import find_packages, setup

setup(
    name="smartermail-api",
    version="0.8.0",
    author="Zachary Sylvester",
    author_email="zacharysylvester81@gmail.com",
    description="This is a simple python wrapper for the SmarterMail API.",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    url="https://github.com/zjs81/SmarterToolsPythonWrapper",
)
