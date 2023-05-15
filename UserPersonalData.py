import tkinter as tk
import ResponseAI
import subprocess

# Define a class to store the data
class User:
    def __init__(self, age, height, name, hobbies, fav_anime, personality):
      self.age = age
      self.height = height
      self.name = name
      self.hobbies = hobbies
      self.fav_anime = fav_anime
      self.personality = personality

# Create a window
window = tk.Tk()

# Make the window wider
window.geometry("500x300")

def senddata():
  # Get the answers from the entry boxes
  age = age_entry.get()
  height = height_entry.get()
  name = name_entry.get()
  hobbies = hobbies_entry.get()
  fav_anime = fav_anime_entry.get()
  personality = personality_entry.get()
  
  # Create a dictionary to store the user's data.
  user_data = {
    "age": age,
    "height": height,
    "name": name,
    "hobbies": hobbies,
    "fav_anime": fav_anime,
    "personality": personality
  }

  # Check if all of the questions have been answered
  if not age or not height or not name or not hobbies or not fav_anime or not personality:
    tk.messagebox.showerror("Error", "Answer all of the questions")
    return

  # Check if the age and height are integers
  try:
    int(age)
    float(height)
  except ValueError:
    tk.messagebox.showerror("Error", "Put a number")
    return

  # Create a new user object
  user = age + ", " + height + ", " + name + ", " + hobbies + ", " + fav_anime + ", " + personality

  #Print the user's data
  #print(user)
  
  window.destroy()
  ResponseAI.getdata(user)
  
  with open("input.txt", "w") as f:
    f.write("")
    
  with open("output.txt", "w") as f:
    f.write("")
  #subprocess.run(["python", "ResponseAI.py"])


# Create labels for each question
age_label = tk.Label(text="What is your age?")
height_label = tk.Label(text="What is your height? (cm)")
name_label = tk.Label(text="What is your name?")
hobbies_label = tk.Label(text="What are your hobbies?")
fav_anime_label = tk.Label(text="What is your favorite anime?")
personality_label = tk.Label(text="What is your personality?")

# Create entry boxes for each answer
age_entry = tk.Entry()
height_entry = tk.Entry()
name_entry = tk.Entry()
hobbies_entry = tk.Entry()
fav_anime_entry = tk.Entry()
personality_entry = tk.Entry()

# Create a button to send data
senddata_button = tk.Button(text="SendData", command=senddata)

# Create a frame to hold all of the widgets
frame = tk.Frame()

# Add the labels, entry boxes, and buttons to the frame
frame.pack()
age_label.pack()
age_entry.pack()
height_label.pack()
height_entry.pack()
name_label.pack()
name_entry.pack()
hobbies_label.pack()
hobbies_entry.pack()
fav_anime_label.pack()
fav_anime_entry.pack()
personality_label.pack()
personality_entry.pack()
senddata_button.pack()


# Run the main loop
window.mainloop()