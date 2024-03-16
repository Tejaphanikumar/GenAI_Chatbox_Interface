import openai
import os
import func as f
import gradio as gr

# Set  API key
openai.api_key = os.environ.get("Enter_Your_API_KEY")

def chatbot(input_text):
    # Generate text response
    fun = func.functions
    text_response = fun.generate_text((input_text))
    choice = input("Want an Image? Enter choice YES/NO:")
    if choice.upper() == "YES":
        # Generate image URL
        image_url = fun.generate_image(input_text)
        return text_response, image_url
    else:
        return text_response, None

# Create input component
input_text = gr.Textbox(lines=4, label="Input Text")

# Create chatbot interface
gr.Interface(chatbot, inputs=input_text, outputs=["text", "text"], title="Chatbot", description="Generate text and image based on input text").launch()
