from setuptools import setup
setup(
    name='keepers',
    description=
    'Keepers - Find resources to determine if you want to keep them',
    py_modules=['keepers'],
    version='0.1.2',
    license='MIT',
    install_requires=[
        'boto3',
    ],
    download_url='https://github.com/acaire/keepers/archive/0.1.2.tar.gz',
    url='https://github.com/acaire/keepers',
    author='Ash Caire',
    author_email='ash.caire@gmail.com',
    keywords=[
        'finders', 'keepers', 'resource', 'discovery', 'aws', 'cloudformation',
        'stacks'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
