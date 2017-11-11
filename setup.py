from setuptools.command.install import install
from os import system
from setuptools import setup
import subprocess

class MyInstall(install):
    def run(self):
        a = subprocess.check_output([
            'apt-get',
            'install',
            '-y',
            'glibc'
        ])
        install.run(self)
# in the setup function:
cmdclass={'install': MyInstall}
setup(cmdclass=cmdclass)
