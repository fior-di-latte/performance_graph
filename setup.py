import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='performance_graph',
     version='0.1.2',
     author="Felix Plagge",
     scripts=['performance_graph/performance_graph.py'],
     author_email="felix.plagge@gmail.com",
     description="Provides visual performance overview of scripts",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="www.google.de",
     packages=['performance_graph'],
    install_requires=['gprof2dot'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )