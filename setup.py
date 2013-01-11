from setuptools import setup
from setuptools import find_packages


long_description = (open('README.md').read()  )


setup(
    name='PkpassStaticWebServer',
    version='0.1', 
    description='a static server can server pkpass file', 
    long_description=long_description,
    author='tim',
    author_email='tim.yellow@gmail.com',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pkpass-static-web-server= pkpass_static_web_server:main',
        ]
    },
