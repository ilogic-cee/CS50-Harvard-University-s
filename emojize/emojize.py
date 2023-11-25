import requests
import bs4

# Fetch the emoji definitions from the HTML page
url = "https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias"
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content
soup = bs4.BeautifulSoup(response.content, "html.parser")

# Create a dictionary to map emoji codes and aliases to their corresponding emojis
emoji_map = {}
for code_alias in soup.find_all("li", class_="code-alias"):
    code = code_alias.text.strip()
    emoji = code_alias.find_previous_sibling("img")["alt"]
    emoji_map[code] = emoji_map.get(code, "") + emoji

def emojize(text):
    # Replace emoji codes and aliases with their corresponding emojis
    emoji_search = re.compile(r":(\w+:)")
    for match in emoji_search.finditer(text):
        code = match.group(1)
        emoji = emoji_map.get(code, "")
        text = text.replace(match.group(0), emoji)
    return text

# Prompt the user for input text
text = input("Enter text to emojize: ")

# Emojize the input text
emojized_text = emojize(text)

# Print the emojized text
print(f"Emojized text: {emojized_text}")
