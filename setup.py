from setuptools import setup, find_packages

setup(
    name="package_for_lesson",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # список залежностей вашого пакету, якщо вони є
    ],
    author="Volodymyr Dzimina",
    author_email="vova.dzimina@gmail.com",
    description="This is a test package for python lessons",
    long_description="This package created for my python lessons with Dmitro Probachai",
    url="https://github.com/41cha/package_for_lesson",
)