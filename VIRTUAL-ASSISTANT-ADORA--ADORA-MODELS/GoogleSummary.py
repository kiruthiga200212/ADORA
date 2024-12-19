import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import Main

def search_and_speak(query):
    try:
        query = query.replace("adora", "").strip()
        if query.startswith("what is"):
            query = query.replace("what is", "").strip()
            search = wikipedia.summary(query, sentences=2)
            Main.Speak(f"According to Wikipedia: {search}")
        elif query.startswith("how to"):
            query = query.replace("how to", "").strip()
            max_results = 1
            how_to_results = search_wikihow(query=query, max_results=max_results)
            if how_to_results:
                Main.Speak(how_to_results[0].summary)
            else:
                Main.Speak("No relevant results found on wikiHow.")
        else:
            pywhatkit.search(query)
    except wikipedia.exceptions.DisambiguationError as e:
        Main.Speak(f"Disambiguation: {', '.join(e.options)}")
    except wikipedia.exceptions.PageError:
        Main.Speak(f"No Wikipedia page found for '{query}'")
    except Exception as e:
        Main.Speak(f"An error occurred: {str(e)}")

# Example usage
search_and_speak("what is photosynthesis")
