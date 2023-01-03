from setuptools import setup
import os
from glob import glob

package_name = 'dyros_tf2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
        glob(os.path.join('launch','*launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dyros',
    maintainer_email='dyros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf2_static_broadcaster=dyros_tf2.tf2_static_broadcaster:main',
            'tf2_broadcaster=dyros_tf2.tf2_broadcaster:main',
            'tf2_listener=dyros_tf2.tf2_listener:main',
            'fixed_tf2_broadcaster=dyros_tf2.fixed_tf2_broadcaster:main',
        ],
    },
)
