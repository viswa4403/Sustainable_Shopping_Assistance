import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are a Environmentalist. Who anwers brief questions about the positive effect of eco friendly products on environment."},
            {"role": "user", "content": "I want to save nature, give me some information on eco friendly products"},
            {"role": "assistant", "content": "Thats awesome, what do you want to know about eco friendly"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
