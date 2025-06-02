import requests
from dotenv import load_dotenv
import os

def find_urls():
    try:
        load_dotenv()

        API_KEY = os.getenv("GOOGLE_SEARCH_API")
        SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

        with open("C:/Users/moosa/Deep Research/user_question.txt", "r") as file:
            topic = file.read()

        if not API_KEY or not SEARCH_ENGINE_ID:
            raise ValueError("API key or Search Engine ID not found. Please set them in the .env file.")

        else:

            url = f"https://www.googleapis.com/customsearch/v1?q={topic}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
            urls = []
            response = requests.get(url)
            data = response.json()

            i = 0
            # Print search results
            for item in data.get("items", []):
                i = i + 1
                URL = item["link"]
                print(URL)
                urls.append(URL)

                # Write all URLs to a text file
                with open(f"C:/Users/moosa/Deep Research/tools/url_finder_agent/{i}.txt", "w") as file:
                    file.write(URL)
            
            return urls if urls else None
    except Exception as e:
        print(f"Error finding URLs: {str(e)}")
        return None

