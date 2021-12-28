from setuptools import find_packages, setup

setup(
    name='clci',
    packages=find_packages(include=['clci']),
    version='0.1.0',
    description='Classical cryptography algorithms',
    author='astrica1',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)