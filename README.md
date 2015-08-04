#Welcome to Checkmate!

[![Build Status](https://travis-ci.org/quantifiedcode/checkmate.svg?branch=master)](https://travis-ci.org/quantifiedcode/checkmate)
[![PyPi version](https://pypip.in/v/checkmate/badge.png)](https://pypi.python.org/pypi/checkmate)
[![PyPi downloads](https://pypip.in/d/checkmate/badge.png)](https://pypi.python.org/pypi/checkmate)
[![Code Issues](http://www.quantifiedcode.com/project/gh:quantifiedcode:checkmate/badge.svg)](http://www.quantifiedcode.com/app#/project/gh:quantifiedcode:checkmate)

##About
Checkmate is a cross-language (meta-)tool for static code analysis, written in Python. Unlike other tools, it provides a global overview of the code quality in a project and aims to provide clear, actionable insights to the user.

###Keypoints

* Provides a global overview of code quality in a project
* Plays nicely with 3rd party libraries and checkers (e.g. pylint, pep8, jslint, etc.)
* Keeps analysis results in a document-oriented database and allows for fast querying
* Can be easily extended to new code checkers or version control systems by creating plugins

###Current Status

The first working version of the tool nears completion, please be patient :)

---------------

## How to contribute

Contributions are very welcome, and are greatly appreciated! Every little bit helps, and credit will always be given. Please read [here](/CONTRIBUTING.md), how you can contribute.

## Get Started!
Are you ready to contribute? Here's how to set up `checkmate` for local development.

1. First, make sure [MongoDB](http://docs.mongodb.org/manual/installation/) is installed on your machine.

2. Fork the `checkmate` repo on GitHub.

3. Clone your fork locally:

        $ git clone git@github.com:<your_github_user_name>/checkmate.git

4. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

        $ mkvirtualenv checkmate
        $ cd checkmate/
        $ sudo python setup.py build install

5. Create a separate branch for each issues in your local development environment:

        $ git checkout -b issue/<issue_id>_<issue_title>

        Example:$ git checkout -b issue/112_add_jslint

6. Now, make your changes locally.

7. When you're done with your changes, please commit and push them to your branch:

        $ git add .
        $ git commit -m "Fix <issue_id>: detailed description of your changes."
        $ git push origin issue/<issue_id>_<issue_title>

8. Submit a Pull Request through the GitHub website.

## Pull Request Guidelines

Before you submit a Pull Request, check that it meets these guidelines:

1. Check on [https://www.quantifiedcode.com/app#/project/gh:quantifiedcode:checkmate](Quantifiedcode) whether your code is free of errors (no login required).

2. The Pull Request should include tests.

3. If the Pull Request adds functionality, also the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.rst.

4. The Pull Request should work for Python 2.6, 2.7, and 3.3, and for PyPy. Check [https://travis-ci.org/quantifiedcode/checkmate/pull_requests](https://travis-ci.org/quantifiedcode/checkmate/pull_requests) and make sure that the tests pass for all supported Python versions.

## Tips

To run a subset of tests:

    $ python -m unittest tests.test_checkmate

## Licences

* Checkmate is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE (Version 3). To view a copy of this license, visit [http://www.gnu.org/licenses/agpl-3.0.html](http://www.gnu.org/licenses/agpl-3.0.html).

* [![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc/4.0/)
Checkmate's documentation by [QuantifiedCode UG (haftungsbeschränkt)](https://github.com/quantifiedcode/checkmate) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

## Questions?

If you have any questions, please get in touch with us:

* [Email](https://www.quantifiedcode.com/contact)
* [@quantifiedcode](https://twitter.com/quantifiedcode)
