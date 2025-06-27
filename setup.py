from typing import List
from setuptools import setup, find_packages
def get_requirements() -> List[str]:
    requirements_list : List[str] = []
    
    with open("requirements.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line and line != "-e .":
                requirements_list.append(line)
    return requirements_list

setup(
    name="AI-Trip-Planner",
    version = "0.0.1",
    author = "Manas Agarwal",
    author_email="manasmrt10@gmail.com",
    description="This project aims at building an agent that can create Travel Itenary for a user based on real time data extracted using various tools/APIs",
    packages=find_packages(),
    install_requires = get_requirements()
)

if __name__ == "__main__":
    rl = get_requirements()
    print(rl)