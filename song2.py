def woohoo(amt):
    for index in range(amt):
        print("Woo hoo!")
        
def yeah(amt):
    for index in range(amt):
        print("Yeah, yeah")
    print("Oh yeah")
    
def verse1():
    print("I got my head checked")
    print("By a jumbo jet")
    print("It wasn't easy")
    print("But nothing i-is, no")
    
def chorus():
    woohoo(1)
    print("When I feel heavy metal")
    woohoo(1)
    print("And I'm pins and I'm needles")
    woohoo(1)
    print("Well I lie and I'm easy")
    print("All of the time but I'm never sure why I need you")
    print("Pleased to meet you")
    
def verse2():
    print("I got my head down")
    print("When I was young")
    print("It's not my problem")
    print("It's not my problem")

def sing_song():
    woohoo(4)
    verse1()
    chorus()
    verse2()
    yeah(3)
    
sing_song()