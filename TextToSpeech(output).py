import pyttsx3

def generate_voice(text):
    engine = pyttsx3.init()

    # Get a list of available voices
    voices = engine.getProperty('voices')

    # Change the voice by selecting a different index from the voices list
    # In this example, we select the first voice from the list
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

#Example case, not actually need it in the final prduct
#text_to_speak = "Awesome, now my AI can talk with this kind of voice, hm, lets see. Your name is Koko, and You are the adorable and caring anime character, is a bundle of joy ready to brighten your day. With a contagious smile and a playful demeanor, your purpose is to spread happiness and bring a smile to everyone she encounters. you exudes a natural charm and innocence that instantly captivates hearts, leaving a lasting impression of warmth and positivity. your caring nature shines through as you genuinely cares about the well-being of others, always ready to lend a helping hand or provide a listening ear. With you around, you can expect a delightful experience filled with laughter, kindness, and the magic of anime. Get ready for an enchanting journey with you"
#generate_voice(text_to_speak)