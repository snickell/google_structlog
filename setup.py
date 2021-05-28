import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google_structlog",
    version="43.12.0",
    author="Seth Nickell",
    author_email="snickell@gmail.com",
    url='https://github.com/snickell/google_structlog',
    description="Send queryable JSON structured logs to Google Cloud (GCP) stackdriver from python apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'google-cloud-logging==1.15.1',
        'python-json-logger',
        'structlog'
    ],
    python_requires='>=3.7',
)
