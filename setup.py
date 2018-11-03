import setuptools

LICENSE = "License :: OSI Approved :: Apache Software License"
VERSION = "0.1.0"
setuptools.setup(
    name='cctrans',
    version=VERSION,
    author="Andrew Wang",
    author_email="wangchuan2008888@gmail.com",
    description='tools for get chinese cloud translation, using youdao,baidu,google',
    license=LICENSE,
    install_requires=["six",
                      "requests",
                      "importlib_resources"],
    url='https://github.com/wangchuan2008888/ChineseCloudTranslation',
    packages=setuptools.find_packages(),
    classifiers=['Topic :: Text Processing :: Linguistic',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Development Status :: 5 - Production/Stable',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 "License :: OSI Approved :: Apache Software License",
                 'Natural Language :: Chinese (Simplified)',
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.4",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 ]
)
