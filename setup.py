from setuptools import setup

setup(
    name='deving',
    packages=[
        'deving',
        'deving.lib',
    ],
    version='0.1.0',
    description='Some dev tools',
    author='Oren',
    author_email='orenovad@gmail.com',
    url='https://github.com/orenovadia/deving',
    install_requires=[
        'click',
        'tqdm',
        'enum34',
    ],
    entry_points={
        'console_scripts': [
            'deving_tracebacks = deving.main:find_exceptions',
        ],
    }
)
