from setuptools import setup, find_packages

setup(
    name="GoogleAPIUtils",
    version="0.1",
    author="Adam Cunnington, MEC UK",
    author_email="adam.cunnington@mecglobal.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["google-api-python-client", "httplib2", "oauth2client"]
)
