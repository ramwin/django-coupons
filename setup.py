import os
from setuptools import setup, find_packages

import coupons


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django2-coupons',
    version=coupons.__version__,
    description='A reuseable Django application for coupon gereration and handling.',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver & Xiang Wang',
    author_email='ramwin@qq.com',
    url='https://github.com/ramwin/django-coupons',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        "django >= 1.11, < 3",
        "djangorestframework >= 3.10",
        "django-filter",
    ],
)
