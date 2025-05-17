from setuptools import setup, find_packages

setup(
    name="task_vector_json",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "project_cli=project.project_cli:app",
        ],
    },
    python_requires=">=3.7",
)
