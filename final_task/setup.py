from setuptools import setup, find_packages

setup(name='pycalc',
      version='1.5.2',
      description='pure line-command calculator',
      author='Nikita Samak',
      author_email='samak.n2@example.com',
      packages=find_packages(exclude=['pycalc.tests']),
      zip_safe=False,
      entry_points={'console_scripts': ['pycalc = pycalc.pycalc:main']}
      )
