import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='citram-python-api',
    version='1.0.3',
    author='José Vicente Mellado',
    author_email='contact@jvm16.xyz ',
    description='Regional Consortium of Transportation for Madrid API wrapper',
    keywords='madrid transport api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jvicentem/citram-python-api',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['zeep==3.4.0',
                      'xmltodict==0.12.0',
                      'requests==2.22.0']
)
