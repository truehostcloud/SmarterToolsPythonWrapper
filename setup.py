from setuptools import find_packages, setup

setup(
    name="smartermail-api",
    version="0.3.0",
    description="This is a simple python wrapper for the SmarterMail API.",
    author="Zachary Sylvester",
    license="Apache License 2.0",
    packages=find_packages(include=["api/smapi.py", "api/mixins"]),
    install_requires=["requests"],
    project_urls={
        "Source": "https://github.com/zjs81/SmarterToolsPythonWrapper",
    },
)
