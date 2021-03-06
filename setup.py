from setuptools import setup, find_packages

from ats_sms_operator.version import get_version

setup(
    name='django-ats-sms-operator',
    version=get_version(),
    description="ATS SMS operator library.",
    keywords='django, sms receiver',
    author='Lubos Matl',
    author_email='matllubos@gmail.com',
    url='https://github.com/matllubos/django-ats-sms-operator',
    license='LGPL',
    package_dir={'ats_sms_operator': 'ats_sms_operator'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU LESSER GENERAL PUBLIC LICENSE (LGPL)',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'django>=1.6',
        'beautifulsoup4>=4.4.0',
        'html5lib>=0.999999',
        'django-ipware>=1.0.0',
    ],
    zip_safe=False
)
