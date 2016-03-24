# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages


IS_PY3 = sys.version_info > (3,)

setup_requires = (
    'pytest-runner',
    )
install_requires = (
    'psycopg2',
    )
tests_require = [
    'pytest',
    ]
extras_require = {
    'test': tests_require,
    }
description = ""

if not IS_PY3:
    tests_require.append('mock==1.0.1')

setup(
    name='cnx-db',
    version='0.1.0',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/cnx-db",
    license='LGPL, See also LICENSE.txt',
    description=description,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    test_suite='cnxdb.tests',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        },
    entry_points="""\
    """,
    )
