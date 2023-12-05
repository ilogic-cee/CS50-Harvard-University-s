from django.shortcuts import render, redirect
import markdown
from .forms import CreateEntryForm
from .utils import save_entry, get_entry, list_entries, convert_md_to_html
import logging
from .models import Entry
from . import util
from django.http import Http404
from .forms import EditEntryForm  # Assuming you have a form for editing entries
from django.views import View
from django.shortcuts import get_object_or_404
import random






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


#def edit_entry(request, entry_title):

def edit_entry(request, entry_title):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

    else:
        # Handle GET request or redirect to an appropriate page
        # You might want to redirect to the entry page or show an error message
        return render(request, "encyclopedia/some_error_page.html")

    # Get the entry or raise a 404 error if it doesn't exist
 #   entry = get_object_or_404(Entry, title=entry_title)

 #   if request.method == 'POST':
        # Handle form submission
    #    form = EditEntryForm(request.POST, instance=entry)
    #    if form.is_valid():
    #        form.save()
    #        print("Form saved successfully")
    #        return redirect('entry', title=entry_title)  # Redirect to the updated entry page
    #    else:
     #       print("Form is invalid:", form.errors)
  #  else:
   #     # Render the form with the existing entry data
  #      form = EditEntryForm(instance=entry)

 #   return render(request, 'encyclopedia/edit.html', {'form': form, 'title': entry_title})




def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html",{
        "title": title,
        "content": html_content
    })

# views.py
class MyView(View):
    def some_method(self):
        from .models import Entry  # Import within the method
        entry_instance = Entry.objects.get(pk=1)
        # Your code here

def custom_random_page(request):
    random_entry_title = rand()
    html_content = convert_md_to_html(random_entry_title)
    return render(request, "encyclopedia/entry.html", {
        "title": random_entry_title,
        "content": html_content
    })
