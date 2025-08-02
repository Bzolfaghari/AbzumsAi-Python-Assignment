from openai import OpenAI

OPENAI_API_KEY = "aa-i1l08MOBQCjEAU7N5Lqn6yDHRRRKqIKCKuZpyrZyFuwZZR2b"
AVALAI_BASE_URL = "https://api.avalai.ir/v1"

client = OpenAI(api_key=OPENAI_API_KEY, base_url=AVALAI_BASE_URL)

# 1. گرفتن لحن و اعتبارسنجی آن
tone = input("Enter the tone for the conversation (e.g., sarcastically, cheerfully, angrily): ")
if not tone.strip():
    print("Error: Tone cannot be empty. Please enter a valid tone.")
    exit(1)

# 2. تعریف تاریخچه با پرامپت سیستمی (برای لحن)
prompts = [
    {'role': 'system', 'content': [{'type': 'text', 'text': f"Respond {tone.strip()}!"}]}
]

EXIT_WORDS = {"quit", "exit", "stop"}

while True:
    # 3. گرفتن پیام از کاربر
    user_message = input("\nEnter your message (or 'quit', 'exit', or 'stop' to end): ")
    if user_message.lower() in EXIT_WORDS:
        print("Ending conversation.")
        break

    if not user_message.strip():
        print("Error: Message cannot be empty. Please enter a valid message.")
        continue

    prompts.append({
        'role': 'user',
        'content': [{'type': 'text', 'text': user_message}]
    })

    try:
        # 4. گرفتن جواب AI با مدل GPT-4.1-nano
        response_obj = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=prompts
        )
        response = response_obj.choices[0].message.content

        print(f"\nAI Response ({tone}): {response}")

        # 5. افزودن پاسخ AI به تاریخچه
        prompts.append({
            'role': 'assistant',
            'content': [{'type': 'text', 'text': response}]
        })

        # 6. نمایش کل تاریخچه مکالمه
        print("\nConversation History:")
        for msg in prompts:
            role = msg['role'].capitalize()
            msg_content = " ".join([part['text'] for part in msg['content']])
            print(f"{role}: {msg_content}")
    except Exception as e:
        print(f"An error occurred: {e}")
