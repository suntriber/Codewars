"""
Welcome to the Mathematics gameshow. I'm your host, Apex Rhombus, and it's time for the lightning round!

Today we'll talk about a hypothetical bottle. This entire bottle weighs 120 grams. Its contents weigh twice as much as the bottle itself. What, may I ask, do the contents weigh?

...Did you guess 80 grams? Correct! Now that you've got that idea, I'm gonna ask you that question in 10 different ways so you'd better get ready!

Let's make a contentWeight function that takes in two parameters: bottleWeight and scale. This function will return the weight of the contents inside the bottle.

bottleWeight will be an integer representing the weight of the entire bottle (contents included).

scale will be a string that you will need to parse. It will tell you how the content weight compares to the weight of the bottle by itself. 
2 times larger, 6 times larger, and 15 times smaller would all be valid strings (smaller and larger are the only comparison words).

The first test case has been filled out for you. Good luck!
"""

def main():
    print(content_weight(120, "2 times larger"), 80)
    print(content_weight(180, "2 times larger"), 120)
    print(content_weight(500, "9 times larger"), 450)
    print(content_weight(1000, "49 times larger"), 980)
    print(content_weight(1000, "999 times larger"), 999)

    print(content_weight(120, "2 times smaller"), 40)
    print(content_weight(300, "2 times smaller"), 100)
    print(content_weight(1000, "4 times smaller"), 200)
    print(content_weight(1000, "49 times smaller"), 20)
    print(content_weight(10000, "999 times smaller"), 10)


def content_weight(bottle_weight, scale):
    """
    s = scale.split(" ")
    if s[2] == 'larger':
        return int((bottle_weight / (int(s[0])+1)) * int(s[0]))
    else:
        return int((bottle_weight / (int(s[0])+1)))
    """
    
    return int((bottle_weight / (int(scale.split(" ")[0])+1)) * int(scale.split(" ")[0])) if scale.split(" ")[2] == 'larger' else int((bottle_weight / (int(scale.split(" ")[0])+1)))

    # return b/(int(''.join([i for i in s if i.isdigit()]))+1)*int(''.join([i for i in s if i.isdigit()]))if 'larger'in s else b/(int(''.join([i for i in s if i.isdigit()]))+1)

if __name__ == "__main__":
    main()