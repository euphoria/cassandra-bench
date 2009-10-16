from paver.easy import *
from paver.setuputils import setup, find_packages

setup(
    name='cassandra-bench',
    version='0.1.0',
    description='benchmarking program created for cassandra',
    author='Ryan Svihla',
    author_email='rssvihla@gmail.com',
    url='http://github.com/rssvihla/cassandra-bench',
    download_url='http://github.com/rssvihla/cassandra-bench/downloads',
    packages=find_packages(),
    long_description="""\
        """,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent"
    ],
    keywords="benchmarking, cassandra",
    license="Apache License 2.0",
    install_requires=[
        'setuptools'
    ],
)


def prepare_reports_dir():
    r = path("buildreports")
    if not r.exists():
        r.mkdir()


@task
def test():
    """run cassandra-bench unit tests using nose"""
    prepare_reports_dir()
    sh('nosetests tests/ --with-xunit --xunit-file buildreports/nose-report.xml')

@task
def lint():
    """run pylint against the cassandra-bench source"""
    prepare_reports_dir()
    sh('pylint cassandrabench -f html >> buildreports/lint.html')
