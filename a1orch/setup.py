# ==================================================================================
#  This SW is developed as part of ITU-5G-AI/ML challenge
#  ITU-ML5G-PS-014: Build-a-thon(PoC) Network resource allocation
#  for emergency management based on closed loop analysis
#  Team : RAN-RIC-xApp
#  Author : Deena Mukundan
#  Description : This file has the main implementation of predictor xApp
# ==================================================================================
from setuptools import setup, find_packages

setup(
    name="a1orch",
    version="0.0.2",
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="A1 handler for orchestrator",
    url="",
    install_requires=["requests", "Flask","ricxappframe>=1.1.1,<2.0.0", "joblib>=0.3.2", "connexion[swagger-ui]","statsmodels>=0.11.1", "schedule>=0.0.0", "mdclogpy<=1.1.1", "pandas"],
    entry_points={"console_scripts": ["run-a1orch.py=a1orch.main:start"]},  # adds a magical entrypoint for Docker
)
