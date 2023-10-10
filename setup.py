import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name = 'AdversarialAttacks',
    description='Adversarial Attacks',
    author = 'Varuni',
    author_email = 'buereddyvarunireddy@gmail.com',
    packages = setuptools.find_packages(),
    keyword = ['deeplearning', 'adversarial', 'attack', 'pytorch', 'torch',
               'rpgd', 'eotpgd', 'pgd', 'fgsm', 'cw', 'rfgsm', 'ifgsm', 'iterll',
               'bim', 'stepll', 'deepfool', 'trades', 'fast', 'mifgsm',
               'dlr', 'apgd', 'fab', 'square', 'autoattack', 'difgsm', 'pixle'
              ],
    install_requires=[
        'torch>=1.7.1', 'torchvision>=0.8.2', 'scipy>=0.14.0', 'tqdm>=4.56.1',
        'requests~=2.25.1', 'numpy>=1.19.4',
    ],
    python_requires = '>=3',
    zip_safe = False,
    license="MIT",
    )
