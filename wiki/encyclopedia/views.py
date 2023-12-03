from django.shortcuts import render, redirect
import markdown
from .forms import CreateEntryForm
from .util import save_entry, get_entry, list_entries, convert_md_to_html
import logging

from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content is None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def css_view(request):
    # Load content from the CSS.md file
    title = "CSS"
    content = util.get_entry(title)

    # If the entry doesn't exist, show an error message
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"This entry for {title} does not exist"
        })

    # Convert Markdown to HTML
    html_content = markdown.markdown(content)

    # Render the CSS view
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def git_view(request):
    # Load content from the Git.md file
    title = "Git"
    content = util.get_entry(title)

    # If the entry doesn't exist, show an error message
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"This entry for {title} does not exist"
        })

    # Convert Markdown to HTML
    html_content = markdown.markdown(content)

    # Render the Git view
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def html_view(request):
    return render_entry(request, "HTML")

def python_view(request):
    return render_entry(request, "Python")

def render_entry(request, title):
    # Load content from the respective Markdown file
    content = util.get_entry(title)

    # If the entry doesn't exist, show an error message
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"This entry for {title} does not exist"
        })

    # Convert Markdown to HTML
    html_content = markdown.markdown(content)

    # Render the view for the specific entry
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def django_view(request):
    # Load content from the Django.md file
    title = "Django"
    content = util.get_entry(title)

    # If the entry doesn't exist, show an error message
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"This entry for {title} does not exist"
        })

    # Convert Markdown to HTML
    html_content = markdown.markdown(content)

    # Render the Django view
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })



def search_form(request):
    recommendation = []  # Initialize the recommendation list

    if request.method == "POST":
        entry_search = request.POST.get('q', '')  # Use get() to avoid KeyError
        html_content = convert_md_to_html(entry_search)

        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            # Entry not found, display an error message or redirect to a search results page
            allEntries = util.list_entries()
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)

            return render(request, "encyclopedia/search_form.html", {
                "recommendation": recommendation
            })

    # Handle other cases (e.g., GET requests) if needed
    # return render(request, "encyclopedia/search_form.html")
logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from .forms import CreateEntryForm
from .util import save_entry, get_entry, list_entries, convert_md_to_html

def new_page(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Check if the entry already exists
            existing_entry = get_entry(title)
            if existing_entry is not None:
                return render(request, 'encyclopedia/error.html', {
                    'message': f'The entry "{title}" already exists.'
                })

            # Save the new entry
            save_entry(title, content)

            # Redirect to the new entry's page
            return redirect('entry', title=title)
        else:
            # Form is not valid, you can add additional logic or context data here
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = CreateEntryForm()

    return render(request, 'encyclopedia/new_page.html', {'form': form})


