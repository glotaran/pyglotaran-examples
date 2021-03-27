from setuptools import find_packages
from setuptools import setup

install_requires = [
    "pyglotaran>=0.3.0,<0.4.0",
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
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    author="Joris Snellenburg, Ivo van Stokkum",
    author_email="""j.snellenburg@gmail.com,
                    i.h.m.van.stokkum@vu.nl """,
    license="MIT",
    project_urls={
        "GloTarAn Ecosystem": "https://glotaran.org",
        "Source": "https://github.com/glotaran/pyglotaran_examples",
        "Tracker": "https://github.com/glotaran/pyglotaran_examples/issues",
    },
    python_requires=">=3.8,<3.10",
    packages=find_packages(),
    install_requires=install_requires,
    zip_safe=True,
)
