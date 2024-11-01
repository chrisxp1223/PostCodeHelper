from setuptools import setup, find_packages

setup(
    name='PostCodeHelper',
    version='0.0.1',
    author='CPWang',
    author_email='cpwangx@gmail.com',
    description='POST Code log analysis tool',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
)