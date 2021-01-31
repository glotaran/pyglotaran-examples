from setuptools import find_packages
from setuptools import setup

install_requires = [
    "pyglotaran>=0.2.0",
    "jupyterlab>=2.0.0",
    "matplotlib>=3.0.0",
]


with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="pyglotaran_examples",
    version="0.3.0",
    description="Supplementary package for pyglotaran with (example) plotting code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glotaran/pyglotaran_examples",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    author="Joris Snellenburg",
    author_email="""j.snellenburg@gmail.com""",
    license="MIT",
    project_urls={
        "GloTarAn Ecosystem": "http://glotaran.org",
        "Source": "https://github.com/glotaran/pyglotaran_examples",
        "Tracker": "https://github.com/glotaran/pyglotaran_examples/issues",
    },
    python_requires=">=3.6,<3.9",
    packages=find_packages(),
    install_requires=install_requires,
    zip_safe=True,
)
