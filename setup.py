from setuptools import setup
from typing import List

REQUIREMENT_FILE_NAME = "requirement.TXT"

def get_requirement_list() -> List[str]:
    """
    This function is going to return list of requirement mention in requirement.txt

    return This function ig going to return a list which contain name of the libraries mentioned in requirement.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

Project_Name= "Housing-Predictor"
version = "0.0.1"
AUTHOR = "GOPI PANDIT"
DISCRIPTION = "This is a my first Maching Learing Project"
PACKAGE = ["Housing"]
setup(

name = "Housing-Predictor",
version = "0.0.1",
author=AUTHOR,
description= DISCRIPTION,
packages= PACKAGE,
install_requires = get_requirement_list()

)



