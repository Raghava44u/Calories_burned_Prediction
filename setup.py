from setuptools import setup , find_packages

setup(
name="calories prediction",
version="0.1",
author="Veera Raghavulu",
author_email="raghavadasari44@gmail.com",
description="No des",
long_description=open("README.md").read(),
packages=find_packages,
url="https://github.com/Raghava44u/Calories_burned_Prediction.git",
requires=[
  "pandas",
  "numpy",
  "matplotlib",# intall dependecies here
]

)