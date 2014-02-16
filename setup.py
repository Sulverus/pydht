import os
import sys
from setuptools import setup


if sys.argv[-1] == 'test':
    status = os.system('python tests/tests.py')
    sys.exit(1 if status > 127 else status)


requirements = ['RPi.GPIO>=0.5.4']

def long_description():
    return "DHT 11 v.2 Temperature/Humanity GPIO driver for Raspberrry PI."


setup(
    name='pydht2',
    version='0.5.1',
    description="DHT 11 v.2 Temperature/Humanity GPIO driver for Raspberry PI.",
    long_description=long_description(),
    url='https://github.com/Sulverus/pydht',
    download_url='https://github.com/Sulverus/pydht',
    author="Andrey Drozdov",
    author_email='sulverus@gmail.com',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    packages=['pydht'],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ]
)
