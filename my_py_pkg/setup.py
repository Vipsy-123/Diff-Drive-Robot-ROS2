from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer_email='vipul@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_pub=my_py_pkg.py_publisher:main",
            "py_sub=my_py_pkg.py_subscriber:main",
            "add_two_ints_server=my_py_pkg.add_two_ints_server:main",
            "add_two_ints_client_no_oop=my_py_pkg.add_two_ints_client_no_oop:main",
            "add_two_ints_client=my_py_pkg.add_two_ints_client:main",
            "add_two_ints_client_simple=my_py_pkg.add_two_ints_client_simple:main"
        ],
    },
)
