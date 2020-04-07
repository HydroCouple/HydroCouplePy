from setuptools import find_packages, setup


setup(
    name='hydrocouplepy',
    version='0.0.0.dev',
    description='A python implementation of the HydroCouple interface specifications',
    author='Caleb Buahin',
    author_email='calebgh@gmail.com',
    license='GNU GPL Version 3',
    url='https://github.com/HydroCouple/HydroCouplePy.git',
    packages=find_packages(),
    keywords='',
    classifiers=[
          'Development Status :: 0 - Beta',
          'Environment :: Console',
          'Intended Audience :: Engineers',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
    ]
)