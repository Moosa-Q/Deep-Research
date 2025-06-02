import os
import glob

def remove_files():
    # Find and remove all HTML files in the directory
    directory = "C:/Users/moosa/Deep Research/tools/get_html_agent"
    for filename in glob.glob(os.path.join(directory, "*.html")):
        os.remove(filename)

    directory2 = "C:/Users/moosa/Deep Research/tools/html_to_md_agent"
    for filename in glob.glob(os.path.join(directory2, "*.md")):
        os.remove(filename)

    directory3 = "C:/Users/moosa/Deep Research/tools/url_finder_agent"
    for filename in glob.glob(os.path.join(directory3, "*.txt")):
        os.remove(filename)

    directory4 = "C:/Users/moosa/Deep Research/tools/writer_agent"
    for filename in glob.glob(os.path.join(directory4, "*.md")):
        os.remove(filename)

    file = "C:/Users/moosa/Deep Research/user_question.txt"
    if os.path.exists(file):
        os.remove(file)
