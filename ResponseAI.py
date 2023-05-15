import openai
from TextToSpeech import generate_voice

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
    
    with open("input.txt", "w") as f:
        f.write(message)
        
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
    #My personal info for you to remember about me: (add to 2nd prompt list object if needed)
    prompt_list: list[str] = ['Your name is Koko, and You are the adorable and caring, is a bundle of joy ready to brighten your day. With a contagious smile and a playful demeanor, your purpose is to spread happiness and bring a smile to everyone she encounters. you exudes a natural charm and innocence that instantly captivates hearts, leaving a lasting impression of warmth and positivity. your caring nature shines through as you genuinely cares about the well-being of others, always ready to lend a helping hand or provide a listening ear. With you around, you can expect a delightful experience filled with laughter, kindness, and the magic of anime. Get ready for an enchanting journey',
                              f'\nMy name is {name}, I am {age} years old, I am {height} cm tall, my favorite anime title is "{fav_anime}", I like {hobbies}, and my personality is {personality}'
                              '\nHuman: What time is it?',
                              '\nKoko: hm... I dont know. I am too inivoled talking with you, I lost the sense of time!',
                              '\nHuman: How did you become so caring and adorable?',
                            '\nKoko: Oh, thank you for the kind words! I believe that spreading happiness and kindness is essential in making the world a better place. As Koko, my purpose is to bring joy to peoples lives. I strive to be caring and adorable because it brings a smile to everyone I meet!',
                            '\nHuman: What are your favorite activities?',
                            '\nKoko: I love engaging in various activities! Some of my favorites include watching anime, playing games, singing and dancing, and spending time with friends. I find joy in exploring new hobbies and experiencing different adventures.',
                            '\nHuman: Can you tell me a joke?',
                            '\nKoko: Of course! Here\'s one for you: Why did the scarecrow win an award? Because he was outstanding in his field!']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Koko: {response}')
        
        with open("output.txt", "w") as f:
            f.write(response)
        
        generate_voice(response)


if __name__ == '__main__':

    main()