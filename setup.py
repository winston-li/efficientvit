#!/usr/bin/env python3

"""Setup efficientvit model zoo."""

from setuptools import find_packages, setup


setup(
    name="efficientvit",
    version="0.0.1",
    description="EfficientViT is a new family of vision models for efficient high-resolution vision.",
    url="https://github.com/winston-li/efficientvit",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "opencv-python",
        "torch",
        "torchvision",
        "einops",
        "onnx",
        "onnxsim",
        "onnxruntime",
    ],
)
