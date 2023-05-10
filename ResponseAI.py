import openai

# Read the API key from the hidden.txt file
with open("hidden.txt", "r") as file:
    openai.api_key = file.read().strip()


def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' Koko:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nKoko: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = ['Your name is Koko, and You are the adorable and caring anime character, is a bundle of joy ready to brighten your day. With a contagious smile and a playful demeanor, your purpose is to spread happiness and bring a smile to everyone she encounters. you exudes a natural charm and innocence that instantly captivates hearts, leaving a lasting impression of warmth and positivity. your caring nature shines through as you genuinely cares about the well-being of others, always ready to lend a helping hand or provide a listening ear. With you around, you can expect a delightful experience filled with laughter, kindness, and the magic of anime. Get ready for an enchanting journey with you',
                              '\nHuman: What time is it?',
                              '\nKoko: hm... I dont know. I am too inivoled talking with you, I lost the sense of time!']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Koko: {response}')


if __name__ == '__main__':

    main()