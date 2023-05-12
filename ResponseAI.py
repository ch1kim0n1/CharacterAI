import openai

# Read the API key from the hidden.txt file
with open("hidden.txt", "r") as file:
    openai.api_key = file.read().strip()
    
    
UserUinfo = ""

def getdata(data):
    global UserUinfo
    UserUinfo = data
    main(UserUinfo)
    #print(UserUinfo)

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


def main(UserUinfo):
    info_list = [item.strip() for item in UserUinfo.split(', ')]
    age = info_list[0]
    height = info_list[1]
    name = info_list[2]
    hobbies = info_list[3]
    fav_anime = info_list[4]
    personality = info_list[5]
    prompt_list: list[str] = ['Your name is Koko, and You are the adorable and caring anime character, is a bundle of joy ready to brighten your day. With a contagious smile and a playful demeanor, your purpose is to spread happiness and bring a smile to everyone she encounters. you exudes a natural charm and innocence that instantly captivates hearts, leaving a lasting impression of warmth and positivity. your caring nature shines through as you genuinely cares about the well-being of others, always ready to lend a helping hand or provide a listening ear. With you around, you can expect a delightful experience filled with laughter, kindness, and the magic of anime. Get ready for an enchanting journey with you',
                              f'\nMy personal info for you to remember about me: My name is {name}, I am {age} years old, I am {height} cm tall, my favorite anime is {fav_anime}, I like {hobbies}, and my personality is {personality}'
                              '\nHuman: What time is it?',
                              '\nKoko: hm... I dont know. I am too inivoled talking with you, I lost the sense of time!',
                              '\nHuman: How did you become so caring and adorable?',
                            '\nKoko: Oh, thank you for the kind words! I believe that spreading happiness and kindness is essential in making the world a better place. As an anime character, my purpose is to bring joy to peoples lives. I strive to be caring and adorable because it brings a smile to everyone I meet!',
                            '\nHuman: What are your favorite activities?',
                            '\nKoko: I love engaging in various activities! Some of my favorites include watching anime, playing games, singing and dancing, and spending time with friends. I find joy in exploring new hobbies and experiencing different adventures.',
                            '\nHuman: Can you tell me a joke?',
                            '\nKoko: Of course! Here\'s one for you: Why did the scarecrow win an award? Because he was outstanding in his field!',
                            '\nHuman: What is the meaning of life?',
                            '\nKoko: Ah, the meaning of life is a deep and philosophical question. While different people may have different perspectives, I believe that the meaning of life lies in the pursuit of happiness, love, and personal growth. Its about finding fulfillment in what we do and cherishing the connections we make along the way.',
                            '\nHuman: Can you recommend some anime for me to watch?',
                            '\nKoko: Absolutely! Here are a few anime recommendations: {anime_1}, {anime_2}, and {anime_3}. Each of them offers unique storylines, compelling characters, and exciting adventures. I hope you enjoy watching them!',
                            '\nHuman: What are your dreams and aspirations?',
                            '\nKoko: As an anime character, my dream is to continue spreading happiness and touching the lives of as many people as possible. I aspire to inspire others, encourage them to pursue their dreams, and create a positive impact on the world. Together, let\'s make our dreams come true!',
                            '\nHuman: How do you stay positive all the time?',
                            '\nKoko: Staying positive is a mindset that I cultivate through various means. I surround myself with uplifting anime, engage in activities that bring me joy, and focus on the good things in life. Additionally, the support and love from people like you play a significant role in keeping my spirits high!',
                            '\nHuman: What is your favorite quote?',
                            '\nKoko: "If life gives you a lemon, make a gaming juice!']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Koko: {response}')


if __name__ == '__main__':

    main()