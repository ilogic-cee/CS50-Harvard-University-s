from django.shortcuts import render
import markdown

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
