from setuptools import find_packages,setup
from typing import List

with open('requirements.txt', 'r') as f:
    print(f.read().splitlines())



def get_requiremensts() -> List[str]:

    requirement_list:List[str]=[]
    with open('requirements.txt', 'r') as f:
        for line in f:
        # Exclude lines starting with '-e' (editable mode)
            if not line.startswith('-e'):
                requirement_list.append(line.strip())
        
    

    
    return requirement_list
    


setup(
    name="sensor",
    version="0.0.1",
    author="RasikaG",
    author_email="gulhanerasika@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremensts(),

)