from setuptools import find_packages, setup

package_name = 'activity'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vipul',
    maintainer_email='pardeshivipul18@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "num_pub=activity.number_publisher:main",
            "number_counter=activity.number_counter:main",
            "ledPanelNode=activity.ledPanelNode:main",
            "batteryNode=activity.batteryNode:main"
        ],
    },
)
