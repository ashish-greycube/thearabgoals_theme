from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thearabgoals_theme/__init__.py
from thearabgoals_theme import __version__ as version

setup(
	name="thearabgoals_theme",
	version=version,
	description="Logo for thearablgoals.com",
	author="GreyCube Technologies",
	author_email="admin@greycube.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
