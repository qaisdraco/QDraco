from setuptools import setup, find_packages

setup(
    name='QDraco',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    description='A library for validating user inputs to prevent common security vulnerabilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Qais Abou Shaheen',
    url='https://github.com/qaisdraco/qaisdraco',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
