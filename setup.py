from distutils.core import setup

setup(
    name='ioccontainer',
    packages=['ioccontainer'],  # this must be the same as the name above
    version='1.0.0',
    description='Service container for automatic dependency injection',
    author='Jim Wright',
    author_email='jmwri93@gmail.com',
    url='https://github.com/jmwri/ioccontainer',
    download_url='https://github.com/jmwri/ioccontainer/archive/0.1.tar.gz',
    keywords=['ioc', 'di', 'dependency', 'injection', 'container'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Inversion Of Control',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
)
