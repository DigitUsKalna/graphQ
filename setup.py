from distutils.core import setup
setup(
  name = 'graphQ',         # How you named your package folder (MyLib)
  packages = ['graphQ'],   # Chose the same as "name"
  version = '2.0.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'a library to handel graphs fitting',   # Give a short description about your library
  author = 'Dibyakanti Ta',                   # Type in your name
  author_email = 'dibyakanti22@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/d-kanti/graphQ',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/d-kanti/graphQ/archive/2.0.1.tar.gz',    # I explain this later on
  keywords = ['graph', 'physics', 'fit'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'scipy',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3' ,     #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9' ,     #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8' ,     #Specify which pyhton versions that you want to support
  ],
)
