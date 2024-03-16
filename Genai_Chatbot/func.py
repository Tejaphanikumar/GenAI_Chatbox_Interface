import openai

class functions:
    def generate_text(prompt):
        # Generate text using OpenAI
        text_result = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )
        return text_result.choices[0].text.strip()

    def generate_image(prompt):
        # Generate an image using OpenAI
        image_result = openai.Image.create(
            prompt=prompt,
            n=3,
            # size = "1024x1024"
            size="512x512"
        )
        return image_result["data"][0]["url"]