
run (On Screen): Speaking of the description, down there, you'll find timestamps. Yeah, I got you covered, so you can skip around if you want to revisit any specific part of the demo.

[03:31 - 04:00]
[Enhanced Functionaliy]
Arun (On Screen): Now, let's talk about the enhanced functionality. The Search Google Clone brings not just regular search, but also Google Image Search and Google Advanced Search.
Check out these links in the upper-right corner to switch between them seamlessly.

[04:01 - 04:30]
[Google Image Search]
Arun (Screen Recording): Now, let's explore the Image Search page. You can type in a query, hit search, and voila! You'll be taken to the Google Image search results for that page.

[04:31 - 05:00]
[Google Advanced Search]
Arun (Screen Recording): And here's the Advanced Search page. Just like Google's own, you can input specific search criteria. When you hit the "Advanced Search" button,
you're taken to the search results page for your query.

[05:01 - 05:30]
[Additional Features]
Arun (On Screen): Oh, and check this out! On the main Google Search page, we've got an "I'm Feeling Lucky" button. Clicking this will take you directly to the first search result
for your query, bypassing the normal results page. Now, that's a time-saver!

[05:31 - 06:00]
[Closing Thoughts]
Arun (On Screen): And there you have it, guys. That was a quick tour of the enhanced Search Google Clone project. If you've got questions or thoughts, drop them in the comments below.
Don't forget to check out the timestamps for easy navigation. Until next time, I'm Arun from Mr. Who's the Boss, signing off.

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
