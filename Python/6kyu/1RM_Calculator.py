"""
You just got done with your set at the gym, and you are wondering how much weight you could lift if you did a single repetition. 
Thankfully, a few scholars have devised formulas for this purpose (from Wikipedia) :

Epley
1 RM = w * (1 + (r/30))
​	

McGlothin
1 RM = (100 * w) / (101.3 - 2.67123 * r)
​	
 
Lombardi
1 RM = w * (r**0.10)
"""

def main():
    print(calculate_1RM(135,20),282)
    print(calculate_1RM(200,8),253)
    print(calculate_1RM(270,2),289)
    print(calculate_1RM(360,1),360)
    print(calculate_1RM(400,0),0)

def calculate_1RM(w, r):
    if r == 1:
        return w
    elif r == 0:
        return 0
    else:
        return round(max([w * (1 + (r/30)), (100 * w) / (101.3 - 2.67123 * r), w * (r**0.10)]))




if __name__ == "__main__":
    main()



"""
def calculate_1RM(w, r):
    return (
        w if r == 1 else
        0 if r == 0 else
        round(max(
            w * (1 + r/30),
            100 * w / (101.3 - 2.67123*r),
            w * r**0.10,
        ))
    )
"""
