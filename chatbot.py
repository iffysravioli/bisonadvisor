import openai
#AI Key from Open Ai 
openai.api_key = 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

with open('catalog.txt', 'r') as file:
    catalog_content = file.read()

def chatbot(question):
    response = chatbot.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate GPT-3 model
        prompt=question,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

print("Hello! I'm BisonBot. How can I assist you today? Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'bye':
        print("BisonBot: Goodbye! If you have more questions, feel free to ask later.")
        break

    prompt_with_catalog = f"{user_input}\n\nCatalog Information:\n{catalog_content}"

    response = chatbot(prompt_with_catalog)
    print(f"BisonBot: {response}")
