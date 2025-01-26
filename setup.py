from setuptools import setup, find_packages

setup(
    name="mailosaurrobot",  # Library name (used in pip install)
    version="0.1.0",  # Initial version
    author="Muzammil Khan",
    author_email="muzammilsk90@gmail.com",
    description="A simple library to provide robot framework keywords to utilize mailosaur library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/muzammil2208/mailosaurrobot.git",  # Repository URL
    packages=find_packages(),
    install_requires=[              # Dependencies
        "mailosaur>=7.19.0",
        "robotframework>=5.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
