from setuptools import setup, find_packages

setup(
    name = 'cmd-server',
    version = '0.0.1',
    keywords = ('cube cmd server'),
    description = 'cube cmd server',
    license = 'MIT License',
    install_requires = ['cubi>=0.0.5', 'keep-running'],

    scripts = ['cubi-cmd-server', 'cubi-cmd-server-test'],

    author = 'http://www.liaohuqiu.net',
    author_email = 'liaohuqiu@gmail.com',
    url = 'https://github.com/liaohuqiu/python-cmd-server',

    packages = find_packages(),
    platforms = 'any',
)
