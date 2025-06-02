from tools.url_finder_agent.url_finder_agent import find_urls 
from tools.get_html_agent.get_html_agent import get_html 
from tools.html_to_md_agent.html_to_md_agent import main as html_to_md_convert
from tools.writer_agent.writer_agent import write_report
from tools.editor_agent.editor_agent import edit_report
from tools.remove_files.remove_files import remove_files
from termcolor import colored

def run_research():
    try:
        research_topic = input(colored("[Deep Research]", "magenta", "on_white") + "\nWhat do you want me to research about: ")

        with open("user_question.txt", "w") as file:
            file.write(research_topic)

        print(colored("[URL Finder Agent]", "magenta", "on_white") + "\nFinding URLs...")
        urls = find_urls()
        if not urls:
            raise Exception("No URLs found")

        print(colored("\n[HTML Agent]", "magenta", "on_white") + "\nGetting HTML...")
        html_files = get_html()
        if not html_files:
            raise Exception("Failed to get HTML content")

        print(colored("\n[HTML to MD Agent]", "magenta", "on_white") + "\nConverting HTML to MD...")
        md_files = html_to_md_convert()
        if not md_files:
            raise Exception("Failed to convert HTML to Markdown")

        print(colored("\n[Writer Agent]", "magenta", "on_white") + "\nWriting report...")
        report = write_report()
        if not report:
            raise Exception("Failed to write report")

        print(colored("\n[Editor Agent]", "magenta", "on_white") + "\nEditing report...")
        final_report = edit_report()
        if not final_report:
            raise Exception("Failed to edit report")

        print(colored("\n[Deep Research]", "magenta", "on_white") + "\nDone! Your report is ready.")
        remove_files()
        return True

    except Exception as e:
        print(colored("\n[Error]", "red", "on_white") + f"\nAn error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    run_research()
