from setuptools import find_packages, setup
import os
from glob import glob

package_name = "mytest"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share/", package_name), glob("launch/*launch.py")),
        (os.path.join("share/", package_name), glob("launch/*launch.xml")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="root@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "pub_node = mytest.trial_pub:main",
            "sub_node = mytest.trial_sub:main",
            "pub_audio = mytest.audio:main",
            "sub_robot = mytest.robot_sub:main",
        ],
    },
)
