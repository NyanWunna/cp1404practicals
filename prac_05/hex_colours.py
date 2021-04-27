HEX_COLORS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
              "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "GhostWhite": "#f8f8ff", "GreenYellow": "#adff2f",
              "light": "#eedd82", "linen": "#faf0e6"}

get_color = input("Enter color name: ")

while get_color != "":
    if get_color in HEX_COLORS:
        print(f"{get_color} is {HEX_COLORS[get_color]}")
    else:
        print("Invalid color name")
    get_color = input("Enter color name: ")