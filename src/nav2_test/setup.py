from setuptools import find_packages, setup
import os
from glob import glob

package_name = "nav2_test"

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
    maintainer="user",
    maintainer_email="user@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "key_input_node = nav2_test.key_input_pub:main",
            "send_action_node = nav2_test.send_action_sub:main",
        ],
    },
)
