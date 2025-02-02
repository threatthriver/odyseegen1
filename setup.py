from setuptools import setup, find_packages

setup(
    name="odysee",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
    ],
    author="Xyron Labs",
    description="A lightweight language model implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)
