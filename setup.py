from setuptools import setup, find_packages


setup(
    name="burmese_tools",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[],  # Empty because no external libraries are required
    author="Min Thiha Tun"
    author_email='mtht1794@gmail.com',
    description='Burmese NLP Tools',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license="MIT",
)