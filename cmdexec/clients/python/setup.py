import setuptools

setuptools.setup(
    name="databricks-sql-connector",
    version="0.0.0",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["pyarrow", 'thrift>=0.10.0', "pandas"],
    author="Databricks",
)
