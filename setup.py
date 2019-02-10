from setuptools import setup

setup(
    name='deving',
    packages=[
        'deving',
    ],
    version='0.1.0',
    description='Some dev tools',
    author='Oren',
    author_email='orenovad@gmail.com',
    url='https://github.com/orenovadia/deving',
    install_requires=[
        req.strip()
        for req in open('requirements.txt')
    ],
    entry_points={
        'console_scripts': [
            'dev-main = deving.main:main',
            'dev-tracebacks = deving.main:find_exceptions',
            'dev-histogram = deving.main:histogram',
            'dev-urlencode = deving.main:encode_parameters',
            'dev-counts = deving.line_counts:counts',
            'dev-pstats-merge = deving.pstats_merge:pstats_merge',
        ],
    }
)
