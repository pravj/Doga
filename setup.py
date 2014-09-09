from setuptools import setup

setup(
    name='Doga',
    version='0.0.1',
    description='HTTP log monitoring console for Humans',
    long_description=open('README.md').read(),
    keywords='http log monitor console doga',
    author='Pravendra Singh',
    author_email='hackpravj@gmail.com',
    url='https://github.com/pravj/Doga',
    license='MIT',
    packages=['Doga', 'Doga.config', 'Doga.logs', 'Doga.parsers', 'Doga.interfaces'],
    package_data = {
        'Doga': ['config/config.ini']
    },
    install_requires=[
        "npyscreen >= 4.4.1",
    ],
    entry_points={
        'console_scripts': ['doga = Doga.doga:main']
    }
)
