from distutils.core import setup

setup(
    name='django-adminwidgetswap',
    version='3.0',
    author='David Davis',
    author_email='davisd@davisd.com',
    py_modules=['adminwidgetswap',],
    url='https://github.com/davisd/django-adminwidgetswap/',
    data_files=[('.',['LICENSE'])],
    license='LICENSE',
    description='django-adminwidgetswap allows for dynamically changing the '
        'django admin widget used for a field at runtime.',
    long_description=open('README').read(),
)

