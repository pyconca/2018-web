
How to build
============

This project is ... probably a bit different from typical nikola projects.
We will use node and gulp to first build the SCSS files. After that, we'll use
nikola to make the site.

Here are the versions we use (those on netlify at this time),

Python: 3.6.6
Node: 8.11.4

Assuming you have the above ready, just run the top-level `build.sh` script.
It's the same file that gets run on netlify.

About the SASS and static files. We have a few things inside `src/` folder.
Our gulp task will compile/copy these into the `files/` folder. When we build
nikola, everything inside that will get copied into the `output/` folder which
gets served.

We deliberately keep `files/` as part of our .gitignore list.

