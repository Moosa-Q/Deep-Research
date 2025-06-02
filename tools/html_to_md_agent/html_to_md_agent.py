import cohere
import os
from pathlib import Path
from dotenv import load_dotenv

def convert_html_to_md_individual(html_files, output_dir, prompt_file_path=None):
    cohere_api_key = os.getenv('COHERE_API_KEY')
    co = cohere.Client(cohere_api_key)
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Read the custom prompt file if provided
    custom_prompt = ""
    if prompt_file_path and os.path.exists(prompt_file_path):
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                custom_prompt = f.read()
            print(f"Loaded custom prompt from: {prompt_file_path}")
        except Exception as e:
            print(f"Warning: Could not read prompt file {prompt_file_path}: {e}")
            custom_prompt = ""
    elif prompt_file_path:
        print(f"Warning: Prompt file not found: {prompt_file_path}")
    
    results = {}
    
    for i, html_file in enumerate(html_files, 1):
        try:
            print(f"Processing file {i}/{len(html_files)}: {os.path.basename(html_file)}")
            
            # Read individual HTML file
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Create prompt for this specific file
            if custom_prompt:
                # Use custom prompt with HTML content
                prompt = f"""{custom_prompt}

HTML Content to convert:
{html_content}"""
            else:
                # Fallback to default prompt
                prompt = f"""Convert the following HTML to clean Markdown format:

{html_content}

Please return only the Markdown content."""
            
            # Process this file individually
            response = co.chat(
                model='command-a-03-2025',
                message=prompt,
                max_tokens=4000
            )
            
            # Save the result
            file_stem = Path(html_file).stem
            output_file = Path(output_dir) / f"{file_stem}.md"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            results[html_file] = {
                'status': 'success',
                'output_file': str(output_file)
            }
            
            print(f"✓ Successfully converted {os.path.basename(html_file)} into {output_file}")
            
        except Exception as e:
            results[html_file] = {
                'status': 'error',
                'error': str(e)
            }
            print(f"✗ Error processing {os.path.basename(html_file)}: {e}")
    
    return results

# Main execution code
def main():
    try:
        # Directory containing HTML files
        input_directory = "C:/Users/moosa/Deep Research/tools/get_html_agent"
        output_directory = "C:/Users/moosa/Deep Research/tools/html_to_md_agent"
        prompt_file = "C:/Users/moosa/Deep Research/tools/html_to_md_agent/.prompt.md"  # Path to prompt file
        
        # Find all HTML files in the directory
        required_extension = ".html"
        html_files = [
            os.path.join(input_directory, filename) 
            for filename in os.listdir(input_directory) 
            if filename.endswith(required_extension)
        ]
        
        file_count = len(html_files)
        print(f"Found {file_count} HTML files to convert")
        
        if file_count == 0:
            print("No HTML files found in the directory.")
            return
        
        # Print list of files to be processed
        print("\nFiles to process:")
        for i, file_path in enumerate(html_files, 1):
            print(f"  {i}. {os.path.basename(file_path)}")
        
        # Convert all HTML files to Markdown
        print(f"\nStarting conversion of {file_count} files...")
        results = convert_html_to_md_individual(html_files, output_directory, prompt_file)
        
        # Return list of successful markdown files
        md_files = [r['output_file'] for r in results.values() if r['status'] == 'success']
        return md_files if md_files else None
    except Exception as e:
        print(f"Error converting HTML to MD: {str(e)}")
        return None

    # Summary
    successful = len([r for r in results.values() if r['status'] == 'success'])
    failed = len([r for r in results.values() if r['status'] == 'error'])
    
    print(f"\n=== Conversion Summary ===")
    print(f"Total files: {file_count}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nFailed files:")
        for file_path, result in results.items():
            if result['status'] == 'error':
                print(f"  - {os.path.basename(file_path)}: {result['error']}")

