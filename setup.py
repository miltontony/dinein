from setuptools import setup, find_packages

setup(
    name='dinein',
    version='0.0.1',
    description='DineIn Food and Social App.',
    long_description=open('README.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Milton Madanda',
    author_email='dev@dinein.co.za',
    license='BSD',
    url='http://dinein.io',
    packages=find_packages(),
    dependency_links=[
    ],
    install_requires=[
        'django-social-auth'
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
