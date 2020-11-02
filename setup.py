import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google_structlog",
    version="2.6.2",
    author="Seth Nickell",
    author_email="snickell@gmail.com",
    description="Send queryable JSON structured logs to Google Cloud (GCP) stackdriver from python apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'google-cloud-logging',
        'python-json-logger',
        'structlog'
    ],
    python_requires='>=3.6',
)
