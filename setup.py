from setuptools import find_packages,setup
from typing import list


def get_requirements(file_path:str)->list[str]:

    '''
    this function return the list of requirements",
    '''

    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]


setup(
    name='mlproject',
    version='0.0.1',
    author='Anand',
    author_email='anandtudu0303@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')



)