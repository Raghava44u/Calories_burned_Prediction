from setuptools import setup , find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    '''
    Function to return a list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
name="calories prediction",
version="0.1",
author="Veera Raghavulu",
author_email="raghavadasari44@gmail.com",
description="No des",
long_description=open("README.md").read(),
packages=find_packages,
url="https://github.com/Raghava44u/Calories_burned_Prediction.git",
install_requires=get_requirements('requirements.txt')
 
)