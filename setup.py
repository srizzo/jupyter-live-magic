import setuptools

setuptools.setup(
    name="jupyter-live-magic",
    version='0.1.2',
    url='https://github.com/srizzo/jupyter-live-magic',
    author="Samuel Rizzo",
    author_email='rizzolabs@gmail.com',
    description="A Jupyter Notebook %%magic for periodic auto re-run and refresh of Cells",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        'jupyter',
        'ipywidgets',
        'jupyter-interval-widget'
    ],
    keywords=['ipython', 'jupyter'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ]
)
