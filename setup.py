try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='awss',
    packages=['awss'],
    entry_points={'console_scripts': ['awss=awss:main']},
    version='0.9.3',
    author="Robert Peteuil",
    author_email="robert.s.peteuil@gmail.com",
    url='https://github.com/robertpeteuil/aws-shortcuts',
    description='AWS Shortcuts for Command-Line Instance Control',
    keywords='AWS EC2 instance control ssh',
    license='MIT License: http://www.opensource.org/licenses/mit-license.php',
    install_requires=['boto3>=1.4',
                      'future>=0.14'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration'],
    long_description=long_description

)
