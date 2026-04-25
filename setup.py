from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str) -> list:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    

setup(
    name='my_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Mohd Sameer',
    email='khansameer786004@gmail.com',
    description='A sample Python package'
)