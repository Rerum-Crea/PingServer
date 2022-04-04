import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PingServer",
    version="0.0.16",
    author="Isaac",
    author_email="no_reply@example.com",
    description="Makes creating a server to be pinged easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Necrownyx/PingServer",
    project_urls={
        "Bug Tracker": "https://github.com/Necrownyx/PingServer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)