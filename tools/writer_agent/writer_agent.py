import cohere
from dotenv import load_dotenv
import os
import re

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

def write_report():
    try:
        # Define the directory path
        md_directory = "C:/Users/moosa/Deep Research/tools/html_to_md_agent"
        md_directory1 = "C:/Users/moosa/Deep Research/tools/writer_agent"
        
        # Initialize Cohere client
        co = cohere.Client(cohere_api_key)
        
        # Find all .md files in the directory that contain a number
        md_files = [f for f in os.listdir(md_directory) if f.endswith(".md") and re.search(r'\d', f)]
        
        # Print the count
        print(f"Number of .md files: {len(md_files)}")
        
        # Read the prompt template
        prompt_file_path = os.path.join(md_directory1, ".prompt.md")
        try:
            with open(prompt_file_path, "r", encoding="utf-8") as prompt_file:
                prompt_template = prompt_file.read()
            with open("C:/Users/moosa/Deep Research/user_question.txt", "r", encoding="utf-8") as question:
                user_question = question.read()
        except FileNotFoundError:
            print(f"Warning: .prompt.md file not found at {prompt_file_path}")
            prompt_template = "Please analyze and summarize the following content:\n\n"
        
        # Process each .md file
        reports = []
        for i, filename in enumerate(md_files):
            file_path = os.path.join(md_directory, filename)
            print(f"Processing file {i+1}/{len(md_files)}: {filename}")
            
            try:
                with open(file_path, "r", encoding="utf-8") as research_file:
                    research_text = research_file.read()
                
                # Create the full prompt by combining template with content
                full_prompt = f"{prompt_template}\n\n--- Content from {filename} ---\n{research_text} ---\n\n And here is the question the report you are meant to answer{user_question}"
                
                # Generate report using Cohere
                response = co.generate(
                    model='command-r-plus-08-2024',  # You can change this to other models like 'command-r' or 'command'
                    prompt=full_prompt,
                    max_tokens=2000,  # Adjust as needed
                    temperature=0.7,  # Adjust for creativity vs consistency
                    truncate='END'
                )
                
                # Extract the generated text
                generated_report = response.generations[0].text.strip()
                
                # Store the report with filename reference
                reports.append({
                    'filename': filename,
                    'report': generated_report
                })
                
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                reports.append({
                    'filename': filename,
                    'report': f"Error processing file: {str(e)}"
                })
        
        # Combine all reports into a comprehensive report
        final_report = "# Comprehensive Report\n\n"
        final_report += f"Generated from {len(md_files)} markdown files\n\n"
        
        for i, report_data in enumerate(reports):
            final_report += f"## Report {i+1}: {report_data['filename']}\n\n"
            final_report += report_data['report']
            final_report += "\n\n---\n\n"
        
        # Save the final report
        output_path = os.path.join(md_directory1, "comprehensive_report.md")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(final_report)
        
        print(f"Report generation completed! Saved to: {output_path}")
        return output_path if os.path.exists(output_path) else None
    except Exception as e:
        print(f"Error writing report: {str(e)}")
        return None
