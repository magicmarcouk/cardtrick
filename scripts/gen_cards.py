import os


#
# Function to write out md file
#
def write_card_md(output_path, img, value, suit):
    
    # String containing page title
    title = "%s"%value
    if suit != "":
        title += " of %s"%(suit)
    
    # Create file
    with open(output_path, 'w') as f:
        f.write('---\n')
        f.write('layout: card\n')
        f.write('title: %s\n'%(title) )
        f.write('value: %s\n'%value)
        if suit != "":
            f.write('suit: %s\n'%suit)
        f.write('img: %s\n'%img)
        f.write('---\n')

suits = {
    "c": "Clubs",
    "d": "Diamonds",
    "h": "Hearts",
    "s": "Spades",
}

values = {
    "a":"Ace",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten",
    "j":"Jack",
    "q":"Queen",
    "k":"King",
}

users = [
    "_pgqgcycj",
    "_ajsnsjsk",
    "_rcswcsme",
    "_xqfxeizi",
    "_xhfpovwr",
    "_oyljpxzc",
    "_ledekkko",
    "_echjrdyo",
    "_vfpgcvff",
    "_tgrtocoq",
    "_jsshxiyj",
    "_hqpvztcn",
]

# Generate Cards
for user in users:
    
    #Make directory if doesnt exist
    base_dir = "users/%s/"%user
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    for value in values:
        for suit in suits:
            #
            path = "%s/%s%s.md"%(base_dir,value, suit)
            img = "img/cards/%s%s.png"%(value.upper(), suit.upper())
            write_card_md(path, img, values[value], suits[suit])

    # Generate Joker
    path = "%s/jo.md"%(base_dir)
    img = "img/cards/JO.png"
    write_card_md(path, img, "Joker", "")


