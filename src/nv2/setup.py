from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'nv2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'), glob(os.path.join('launch','*launch.[pxy][yma]'))),
        (os.path.join('share',package_name,'config'), glob(os.path.join('config/*.yaml'))),
        (os.path.join('share',package_name,'config'), glob(os.path.join('config/*.rviz')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='orin',
    maintainer_email='orin@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'navigation  = nv2.navigation :main',
        'example_follow_path  = nv2.example_follow_path :main',
        ],
    },
)
