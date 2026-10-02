"""
Setup script for leaver detection system
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="leaver-detection-agent",
    version="1.0.0",
    author="Insider Risk Analyst",
    description="AI-driven insider threat detection platform for automated leaver investigation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/leaver-detection-agent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=[
        "anthropic>=0.39.0",
        "langgraph>=0.2.45",
        "pydantic>=2.9.2",
        "streamlit>=1.39.0",
        "plotly>=5.24.1",
        "pandas>=2.2.3",
        "faker>=30.8.2",
        "python-dotenv>=1.0.1",
        "pyyaml>=6.0.2",
    ],
    entry_points={
        "console_scripts": [
            "leaver-detect=main:main",
        ],
    },
)
