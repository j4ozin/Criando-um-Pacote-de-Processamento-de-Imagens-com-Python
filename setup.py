from setuptools import setup, find_packages

with open ('README.md', 'r') as f:
    page_description = f.read()
    
with open ('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='my-image-processing',
    version='0.0.1',
    author='João Basante',
    description='Image processing package using Skimage DIO',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/j4ozin',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)