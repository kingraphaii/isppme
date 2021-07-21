from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in isppme/__init__.py
from isppme import __version__ as version

setup(
	name="isppme",
	version=version,
	description="ISPPME Elearning & School Management System",
	author="Percival Rapha",
	author_email="percival@yate.co.zw",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
