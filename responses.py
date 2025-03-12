from random import choice, randint


def get_response(usr_input: str) -> str:
    lowered = usr_input.lower()
    greetings = ["hello", "hi", "hey", "wassup"]
    not_parsed = ["What in TARNATION!!! Repeat that please", "I'm sorry feller can't seem to comrprehend ye say it again", "Could I trouble ya to rephrase that" ]
    rock_paper_scissors = ["rps", "rock, paper, scissors", "rock, paper, and scissors"]
    if lowered.strip() == "":
         return "Well looks like this buckaroos got you toungue tied"
    elif lowered.strip() in greetings:
         return "Howdy, Partner how can I help ya Ol, son?"
    elif lowered == "roll dice":
         return f"You have rolled: {randint(1,6)} Yee-Yee!"
    elif lowered.strip() in rock_paper_scissors:
         rps_list = ["rock", "paper", "scissors"]
         
         bot_play = randint(0,2)
         return rps_list[bot_play]
    else:
         return choice(not_parsed)
         
    
