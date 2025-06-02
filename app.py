import streamlit as st
from tools.url_finder_agent.url_finder_agent import find_urls
from tools.get_html_agent.get_html_agent import get_html
from tools.html_to_md_agent.html_to_md_agent import main as html_to_md_convert
from tools.writer_agent.writer_agent import write_report
from tools.editor_agent.editor_agent import edit_report
from tools.remove_files.remove_files import remove_files

st.title("Open-Source Deep Research 🔍")
st.write("This app is designed to help you conduct deep research on any topic of your choice.")

research_topic = st.text_input("Enter your research topic")
if st.button("Start Research"):
    if research_topic:
        try:
            with open("user_question.txt", "w") as file:
                file.write(research_topic)

            st.info("Finding URLs...")
            urls = find_urls()
            if not urls:
                st.error("No URLs found")
            else:
                st.text_area("Found URLs", value="\n".join(urls), height=200)

            st.info("Getting HTML content...")
            html_files = get_html()
            if not html_files:
                st.error("Failed to get HTML content")
            else:
                # Display HTML content for each file
                for file_path in html_files:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        st.text_area(f"HTML Content from {file_path}", value=content, height=200)

            st.info("Converting HTML to Markdown...")
            md_files = html_to_md_convert()
            if not md_files:
                st.error("Failed to convert HTML to Markdown")
            else:
                # Display markdown content for each file
                for file_path in md_files:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        st.text_area(f"Markdown Content from {file_path}", value=content, height=200)

            st.info("Writing report...")
            report = write_report()
            if not report:
                st.error("Failed to write report")
            else:
                with open(report, 'r', encoding='utf-8') as f:
                    content = f.read()
                    st.text_area("Initial Report", value=content, height=300)

            st.info("Editing report...")
            final_report = edit_report()
            if not final_report:
                st.error("Failed to edit report")
            else:
                with open(final_report, 'r', encoding='utf-8') as f:
                    content = f.read()
                    st.text_area("Final Report", value=content, height=300)

            st.success("Done! Your report is ready.")
            remove_files()

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter a research topic.")
