from setuptools import find_packages, setup

package_name = 'action_py'

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
            "count_until_server=action_py.count_until_server:main",
            "count_until_client=action_py.count_until_client:main",
            "action_challenge_client=action_py.actions_challenge_client:main",
            "action_challenge_server=action_py.actions_challenge_server:main"

        ],
    },
)
