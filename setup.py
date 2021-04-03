from setuptools import setup

setup(name='granim',
      version='0.1',
      description='Plotting animated graphs using manim.',
      long_description='The package helps you plot animated graphs using the manim engine.',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      scripts=['bin/granim-plot'],
      keywords='manim graph plots',
      url='http://github.com/praeclarumjj3/granim',
      author='Jitesh Jain',
      author_email='jitesh_j@cs.iitr.ac.in',
      license='MIT',
      packages=['granim'],
      install_requires=[
          'manimlib',
      ],
      zip_safe=True,
      test_suite='nose.collector',
      tests_require=['nose'])