import setuptools
from os.path import join, dirname


setuptools.setup(
    name="model_mommy",
    version="0.8.1",
    packages=["model_mommy"],
    include_package_data=True,  # declarations in MANIFEST.in
    install_requires=open(join(dirname(__file__), 'requirements.txt')).readlines(),
    tests_require=[
        'django<1.5',
        'pil',
        'tox',
    ],
    test_suite='runtests.runtests',
    author="vandersonmota",
    author_email="vandersonmota@gmail.com",
    url="http://github.com/vandersonmota/model_mommy",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="automatic object creation facility for django",
    keywords="django testing factory python",
)
