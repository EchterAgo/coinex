import setuptools

setuptools.setup(
    name='coinex.py',
    version='1.0.4',
    author='Axel Gembe',
	author_email='derago@gmail.com',
    description='coinex.com API wrapper',
    long_description=open('README.md', 'rt').read(),
	long_description_content_type='text/markdown',
    url='https://github.com/EchterAgo/coinex',
	packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
