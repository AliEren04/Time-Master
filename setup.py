from setuptools import setup, find_packages

setup(
    name="timemaster", 
    version="1.0.0",
    author="Ali Eren Tabak",
    author_email="alierentabak04@gmail.com", 
    description="A high-precision, drift-free time management library providing stopwatch, countdown, and granular time data extraction.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AliEren04/TIMEMASTER",
    packages=find_packages(),
    keywords="timer, stopwatch, countdown, precision, monotonic, beep, cross-platform",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.12', # S
)