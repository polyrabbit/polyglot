from setuptools import setup, find_packages

# see https://github.com/GaretJax/i18n-utils/blob/master/setup.py
# and https://github.com/elastic/curator/blob/master/setup.py
setup(
    name='polyglot',
    version='0.1',
    url='https://github.com/polyrabbit/polyglot',
    license='MIT',
    author='poly',
    author_email='mcx_221@foxmail.com',
    description='A computer language savant',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='any',
    install_requires=open('./requirements.txt').read().split('\n'),
    entry_points={
        "console_scripts": ["polyglot=polyglot.cli:run"]
    }
)
