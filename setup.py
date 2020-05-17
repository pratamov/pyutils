from setuptools import setup, find_packages

requirements = [
    "google-api-python-client",
    "google-auth-oauthlib",
    "google-auth-httplib2",
    "youtube-transcript-api",
    "pymongo",
    "dnspython"
]

setup(
    name="pyutils",
    version="0.0.1",
    description="Python module gado gado",
    url="git@github.com:pratamov/pyutils.git",
    author="Andre Pratama",
    author_email="andre@itguy.id",
    license="propriatery",
    packages=find_packages(),
    install_requires=requirements,
    zip_safe=False,
    python_requires='>3.5.2'
)
