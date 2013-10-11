import os
from setuptools import setup, find_packages
try:  # explicitly check for cffi
    import cffi
except ImportError:
    raise ImportError("Please install cffi first")
import smbus

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(readme) as f:
        long_description = f.read()
setup(
    name='smbus-cffi',
    version='0.1',
    description='This Python module allows SMBus access through the I2C /dev interface on Linux hosts. The host kernel must have I2C support, I2C device interface support, and a bus adapter driver.',
    long_description=long_description,
    author='David Schneider',
    author_email='david.schneider@bivab.de',
    url='https://github.com/bivab/smbus-cffi',
    packages=find_packages(),
    zip_safe=False,
    ext_package='smbus-cffi',
    ext_modules=[smbus.ffi.verifier.get_extension()],
    install_requires=['cffi ==0.6, ==0.7'],
    license='GPLv2',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System :: Hardware',
    ],
)
