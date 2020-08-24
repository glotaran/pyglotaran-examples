from setuptools import setup, find_packages

install_requires = [
    'pyglotaran>=0.1.0',
    'jupyterlab>=2.0.0',
    'matplotlib>=3.0.0',
]


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyglotaran_examples",
    version='0.1.0',
    description='Examples for using pyglotaran',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/glotaran/pyglotaran_examples',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
    author='Joris Snellenburg',
    author_email="""j.snellenburg@gmail.com""",
    license='GPLv3',
    project_urls={
        'GloTarAn Ecosystem': 'http://glotaran.org',
        # 'Documentation': 'https://pyglotaran_examples.readthedocs.io',
        'Source': 'https://github.com/glotaran/pyglotaran_examples',
        'Tracker': 'https://github.com/glotaran/pyglotaran_examples/issues',
    },
    python_requires=">=3.6,<3.9",
    packages=find_packages(),
    install_requires=install_requires,
    zip_safe=True,
)
