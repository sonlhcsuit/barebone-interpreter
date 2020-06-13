#!/usr/bin/env python3
from setuptools import setup


setup(
    name="barebones",
    version="1.0.0",
    description="Interpreter for an extended Barebones language written in Python3 for MrSon",
    author="Luu Hoang Son | Nguyen Tran Trung",
    author_email="18521348@gm.uit.edu.vn |18521555@gm.uit.edu.vn",
    packages=["barebones"],
    entry_points = {
        "console_scripts": ["barebones = barebones:main"]
    }
)
