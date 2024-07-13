from setuptools import find_packages, setup



def get_requirement(file_path) -> list[str]:

    """
    This function will return list of requirements
    """


    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements




setup(

    name="MenuMate",
    version ="0.01",
    author = "Sushant Vijay Shelar",
    author_email= "sushantshelar121@gmail.com",
    packages= find_packages(),
    install_required = get_requirement("requirements.txt")
)