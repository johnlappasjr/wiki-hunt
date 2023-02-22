import wikipedia

# Prompt the user to enter a search query
query = input("Enter a word to search on Wikipedia: ")

# Set the language of the Wikipedia to be searched (default is English)
wikipedia.set_lang("en")

try:
    # Retrieve the summary of the Wikipedia article corresponding to the search query
    summary = wikipedia.summary(query)
    print(summary)
except wikipedia.exceptions.DisambiguationError as e:
    # Handle disambiguation pages (pages that have multiple possible meanings)
    print("The search query may refer to the following pages:")
    options = e.options
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
except wikipedia.exceptions.PageError:
    # Handle cases where the search query does not match any Wikipedia articles
    print("The search query does not match any Wikipedia articles.")
