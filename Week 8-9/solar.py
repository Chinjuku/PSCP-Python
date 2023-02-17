"""pair programming"""
def sun_pos(solar, name="Sun"):
    "get sun position"
    planet = ""
    pos = 0
    for i in solar:
        if i != " ":
            planet += i
        else:
            pos += 1
            if planet == name:
                return pos
            else:
                planet = ""
def get_star(solar, want_pos):
    "get name star"
    planet = ""
    position = 0
    for i in solar:
        if i != " ":
            planet += i
        else:
            position += 1
            if position == want_pos:
                return planet
            else:
                planet = ""
def main():
    """Solar System"""
    solar = input() + " "
    sun_position = sun_pos(solar)
    last_position = solar.count(" ")
    # Hot Star
    if sun_position == 1:
        print("Hot: %s" %get_star(solar, 2))
    elif sun_position == last_position:
        print("Hot: %s" %get_star(solar, last_position-1))
    else:
        print("Hot: %s %s" %(get_star(solar, sun_position-1), get_star(solar, sun_position+1)))
    # Cold Star
    center = (last_position+1)/2
    if sun_position == center:
        print("Cool: %s %s" %(get_star(solar, 1), get_star(solar, last_position)))
    elif sun_position > center:
        print("Cool: %s" %get_star(solar, 1))
    else:
        print("Cool: %s" %get_star(solar, last_position))
main()
