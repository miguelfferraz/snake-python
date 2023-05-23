import re
from os.path import dirname, join
from setuptools import find_packages, setup

with open(join(dirname(__file__), "game", "__init__.py")) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError("Unable to find own __version__ string")

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="snake-python",
    version=version,
    author="Miguel Figueira Ferraz",
    author_email="miguelfigueiraferraz@gmail.com",
    description="Snake game in Python",
    license="MIT",
    url="https://github.com/miguelfferraz/snake-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.10.0",
)
