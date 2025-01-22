from rake_nltk import Rake
import ollama  # Python Ollama library for local Llama model interaction
import yt
import re
client = ollama.Client()
# Function to query Ollama Llama
def query_ollama(prompt, model="llama3"):
    try:
        model='llama3'
        prompt="List the top 10 most important Python topics for a beginner in a Python list format."
        response=client.generate(model=model,prompt=prompt)
        return response.response
    except Exception as e:
        print(f"Error querying Ollama: {e}")
        return None

# Function to extract keywords using RAKE
def extract_keywords_with_rake(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()

# Main logic
def main():
    prompt = "List the top 10 most important webdev topics for a beginner in a Python list format. Therefore, it should have square brackets and the 10 topics should be strings wihtin the brackets"
    response = query_ollama(prompt)
    
    if not response:
        print("No response from Ollama.")
        return
    
    print("Response from Ollama:", response)
    pattern = r'\[.*?\]'
    match = re.search(pattern, response, re.DOTALL)
    if match:
        # Extract the matched list
        response=match.group(0)
    
    # Assuming the response is a Python list format as a string, eval it safely
    try:
        topics = eval(response)  # Ensure Ollama returns a Python list in its response
        if not isinstance(topics, list):
            print("The response is not a valid Python list.")
            return
    except Exception as e:
        print(f"Error parsing Ollama response: {e}")
        return

    # Process each topic with RAKE
    # final_topics = []
    # for topic in topics:
    #     condensed_keywords = extract_keywords_with_rake(topic)
    #     final_topics.append(condensed_keywords[0] if condensed_keywords else topic)

    # print("Final List of Topics:", final_topics)
    # for i in final_topics:
    for i in topics:
        yt.yt_search(i)

if __name__ == "__main__":
    main()