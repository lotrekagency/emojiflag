from setuptools import setup, find_packages


setup(name='emojiflag',
	version='1.0.1',
	url='https://github.com/lotrekagency/emojiflag',
	license='MIT',
	author='Lotrek',
	author_email='dimmitutto@lotrek.it',
	description='Emoji country flags for language codes and LCID\'s',
	long_description=open('README.rst').read(),
	install_requires=[],
	packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
