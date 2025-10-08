import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY value is not found in environment file.check your .env file.")
openai.api_key=OPENAI_API_KEY
def generate_blog(paragraph_topic):
   try:
         response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system","content":"You are a professional blog writer.Write,clear,engaging,and informative paragraph"},
                {"role": "user","content":f"Write a detailed paragraph about the topics:{paragraph_topic}"},
            ],
               
            max_tokens = 50,
            temperature =0.3
            
         )
         generate_text=response.choices[0].message.content.strip()
         return generate_text
   except Exception as e:
       print(f"error generating blog paragraph:{e}")
       return None
      
if __name__ == "__main__":
    topic = "The benefits of sustainable living"  # Change this to test different topics
    print(f"Generating blog paragraph on: {topic}")
    result = generate_blog(topic)
    if result:
        print("\nGenerated Blog Paragraph:\n")
        print(result)
    else:
        print("Failed to generate paragraph. Check the error above.")









