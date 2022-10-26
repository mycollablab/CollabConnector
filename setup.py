from setuptools import setup, find_packages

requires = open('requirements.txt', 'r').readlines()

setup(
    name='CollabConnector',
    version="0.0.1634",
    description='Cisco Collab Libraries for Python',
    url='git@github.com:mycollablab/CollabConnector.git',
    author='Jon Snipes',
    author_email='jon@mycollablab.org',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    zip_safe=False
)