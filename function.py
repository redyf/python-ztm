# Functions
# Default Parameters
def say_hello(name="Darth Vader", emoji="😈"):
    print(f"Hello {name} {emoji}")


# Arguments
say_hello("Mateus", "😊")
say_hello("Tai", "😊")

# Keyword Arguments (considerado como má prática pois pode confundir outros desenvolvedores)
say_hello(emoji="😊", name="Bibi")
say_hello()
