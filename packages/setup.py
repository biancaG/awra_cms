from setuptools import setup

setup(name='awrams',
      packages=['awrams'],
      version='1.2',
      description='AWRA Modelling System (Community Release), version 1.2',
      url='https://github.com/awracms/awra_cms',
      author='awrams team',
      author_email='awrams@bom.gov.au',
      license='AWRA License',
      zip_safe=False,
      include_package_data=True,
      setup_requires=['nose>=1.3.3'],
      test_suite='nose.collector',
      tests_require=['nose'],
      python_requires='==3.6.*',
)
