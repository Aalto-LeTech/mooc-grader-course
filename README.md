A course template for mooc-grader
---------------------------------

Remember to clone the submodules:

    git clone --recursive URL
    # OR in existing repository
    git submodule --init --recursive

The `index.rst` defines the course schedule and content.
It links to module `rst` files that link to chapter `rst`
files. Once loaded to mooc-grader the system can configure
A+ according the course definition.

The `rst` files support special directives defined in
https://github.com/Aalto-LeTech/a-plus-rst-tools

Custom exercise graders can be configured using yaml files.
https://github.com/Aalto-LeTech/mooc-grader/tree/master/exercises
