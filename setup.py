from setuptools import setup, find_packages


setup(
    name="gamelab",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'Flask>=0.12',
        'Flask-APScheduler>=1.7.0',
        'Flask-BasicAuth>=0.2.0',
        'Flask-Bootstrap>=3.3.7.1',
        'Flask-SocketIO>=2.8.6',
        'Flask-SQLAlchemy>=2.1',
        'eventlet>=0.20.1',
        'numpy>=1.11.1',
        'PyYaml>=3.12',
        'thespian>=3.8.0',
    ],
    # metadata for upload to PyPI
    author="Chris Messier",
    author_email="messiercr@gmail.com",
    description="A light-weight interface for mtree.",
    license="MIT",
    keywords="mechanical turk, experiments, data validation",
    url="https://github.com/messiest/gamelab",  # project home page, if any
)
