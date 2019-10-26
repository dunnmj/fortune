import random
from image_utils import ImageText
import os

list_one = [
    "Luckily, the answer ",
    "Unfortunately, the answer ",
    "Congratulations, the answer ",
    "Sorry, but the answer ",
    "The answer to a different question ",
    "A good answer ",
    "Certainly, the answer ",
    "In your dreams, the answer ",
    "Happily, the answer ",
    "Sadly, the answer ",
    "Possibly, the answer ",
    "Your best friend says the answer ",
    "Your worst enemy says the answer ",
    "Your new friend says the answer ",
    "Everyone knows the answer ",
    "Someone you like says the answer ",
    "Someone you trust says the answer ",
    "Someone new says the answer ",
    "Someone you know says the answer ",
    "A little bird says the answer ",
    "The graffiti says the answer ",
    "A private eye says the answer ",
    "A secret admirer says the answer ",
    "A stranger says the answer ",
]

list_two = [
    "is now ",
    "was once ",
    "used to be ",
    "will soon be ",
    "will sometime be ",
    "will always be ",
]

list_three = [
    "\"yes.\"",
    "\"no.\"",
    "\"maybe.\"",
    "not \"yes.\"",
    "not \"no.\"",
    "for you to guess. ",
    "just what you want.",
    "not what you want.",
    "precise.",
    "not precise.",
    "impossible to know.",
    "blowing in the wind.",
    "\"yes,\" but for a limited time only.",
    "\"no,\" but for a limited time only.",
    "\"yes,\" maybe \"no\" later.",
    "\"no,\" maybe \"yes\" later.",
    "written in the tea leaves.",
    "seen in your eyes.",
    "trying to tell you something.",
    "keeping you awake at nights.",
    "messing with your mind.",
    "told better by flipping a coin.",
    "revealed in the future.",
    "\"yes\" and/or \"no.\"",
]




color = (0, 0, 0)
text = 'Python is a cool programming language. You should learn it!'
font = 'PAPYRUS.TTF'
img = ImageText("ornate.jpg", background=(255, 255, 255, 200)) # 200 = alpha


fortune = random.choice(list_one) +  random.choice(list_two) + random.choice(list_three)
img.write_text_box((30, 30), fortune, box_width=290, font_filename=font,
                   font_size=40, color=color, place='center')


img.save('sample-imagetext.png')
os.system("lpr -o orientation-requested=6 sample-imagetext.png")


print fortune