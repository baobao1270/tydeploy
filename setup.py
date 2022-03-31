from setuptools import setup, find_packages

setup(
    name="tydeploy",
    version="1.0.0rc1",
    description="Tianyi's Deploy Tool",
    long_description="Multiprocess deployer supports SSH (SFTP), Tencent COS, Zip and local FS (Chinese Only)",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords="deployer",
    author="Joseph Chris",
    author_email="joseph@josephcz.xyz",
    url="https://github.com/baobao1270/tydeploy.git",
    license="GPL-3.0-or-later",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[req.strip() for req in open("requirements.txt", "r").read().strip().split("\n")],
    entry_points={
          'console_scripts': [
              'tydeploy = tydeploy.tydeploy:main'
          ]
    }
)
