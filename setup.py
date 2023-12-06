from setuptools import setup, find_packages

setup(
    name='buddy',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'openai', 'pyperclip', 'toml'  
    ],
    entry_points={
        'console_scripts': [
            'buddy=buddy.app:main',  
        ],
    },
    author='Sam Segal',
    license='MIT'
)
