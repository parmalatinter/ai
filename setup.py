from setuptools import setup, find_packages

setup(
    name='ai',
    version='0.1.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'ai-test = test.exec:main'
        ]
    }
)

