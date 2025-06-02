import cohere
import os
from dotenv import load_dotenv

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

def edit_report():
    try:
        with open("C:/Users/moosa/Deep Research/tools/writer_agent/comprehensive_report.md", "r", encoding="utf-8") as base_report:
            base_report_text = base_report.read()

        with open("C:/Users/moosa/Deep Research/tools/editor_agent/.prompt.md", "r", encoding="utf-8") as prompt_file:
            prompt_template = prompt_file.read()

        with open("C:/Users/moosa/Deep Research/user_question.txt", "r", encoding="utf-8") as question:
            user_question = question.read()

        prompt = f"Please use the .prompt.md file --> {prompt_template} <--- to edit the report \n\n---{base_report_text} ---\n\n And here is the question the report you are meant to answer: {user_question}"

        co = cohere.Client(cohere_api_key)
        response = co.generate(
            model='command-r-plus-08-2024',  # You can change this to other models like 'command-r' or 'command'
            prompt=base_report_text,
            max_tokens=2000,  # Adjust as needed
            temperature=0.7  # Adjust for creativity vs consistency
        )

        print(response.generations[0].text.strip())
        output_path = "C:/Users/moosa/Deep Research/report.md"
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(response.generations[0].text.strip())
        
        return output_path if os.path.exists(output_path) else None
    except Exception as e:
        print(f"Error editing report: {str(e)}")
        return None
    
edit_report()