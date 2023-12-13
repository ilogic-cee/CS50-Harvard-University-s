hello, world welcome to my YouTube channel, I am IlogicCee jr ,
and this is my submission for cs50 Web Programming with python and JavaScript project 0,

the project is called search, where i had to design a front end for google search, google image search and google advanced search

[Google Search Page]
First off, we've got our Google Search page, Check out the upper-right corner, we have four visible link text in our search page, , which is search, it redirects to the Google Search page, Image search, advanced search and IlogicCee,

[Google Search Functionality]

and here we are, on the search results page for our query Our. search bar is centered with rounded corners, close to Google's.

NOW let's type a query “rugby sa” and hit "Google Search.” button;
[Closing Shot]
[Outro Music Playing]
[Wide shot of Arun reaching to turn off the camera]-

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(8
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
