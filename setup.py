from typing import List

from setuptools import find_packages, setup

REQUIRED_PACKAGES: List[str] = ['flask', 'grpcio', 'grpcio-tools']
DEV_PACKAGES: List[str] = ['mypy']

version = '0.0.1'

setup(
    name='mango',
    version=version,
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description=('Dummy service backed by grpc'),
    extras_require={'dev': DEV_PACKAGES},
)
