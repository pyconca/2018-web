.. title: README
.. slug: readme
.. date: 2018-08-24 20:56:12 UTC+04:00
.. type: text


Website README
##############

Welcome to the Pycon Canada 2018 website source code! If you are reading this,
it is likely that you are a volunteer who wants to help out. Let's get started
shall we?

**Requirements**

+--------+--------+
| Python | 3.6.6  |
+--------+--------+
| NodeJS | 8.11.4 |
+--------+--------+

First off, you'll need to have the above tools installed on your system. When
this project (website) was started, a major motivation was to use Python 3.
Besides that, we just stuck with the versions available on our host - Netlify.

Next, you'll want to clone the repository to your local system. If you want to
submit patches to improve the site, consider forking the project and sending
us a pull request on Github. No promises that we'll accept every suggestion,
but when we do, you'll be able to have a nice warm and fuzzy feeling that you
helped make Pycon Canda that much better! :)

Once the project is cloned to your local system, you'll want to build the site.
Just run the following command,

.. code-block:: shell

   $ ./build.sh

This will install all the NPM and Python dependencies we need. It will also
build the site and place it inside a new `output/` folder inside your project
directory.

At this point you can run,

.. code-block:: shell

   $ nikola serve

To see the site running at http://localhost:8000/
( Ctrl + C to cancel the local server)

As a shortcut the following command can help (works after you've run build.sh
at least once and are not changing any gulp-related stuff),

.. code-block:: shell

   $ nikola clean && nikola build && nikola serve

Speaking of gulp, you might be wondering, why we have it as a dependency? We
use it to process our SASS files into CSS. And to inherit styles from the
Bootstrap 4 project.

We put all our SASS stuff inside the `src/` folder. Gulp will then process it
into CSS and put it inside a top-level `files/` folder. Nikola will use this
as static material and copy it over to the `output/` directory.

If you haven't guessed it by now, we build most of the site using Nikola, the
static site generator - made with Python! :)
