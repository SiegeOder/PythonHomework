from setuptools import setup, find_packages

setup(name='pycalc',
      version='1.6.4',
      description='pure line-command calculator',
      author='Nikita Samak',
      author_email='samak.n2@gmail.com',
      packages=find_packages(exclude=['pycalc.tests']),
      zip_safe=False,
      entry_points={'console_scripts': ['pycalc = pycalc.pycalc:main']}
      )
