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
    "C": "Clubs",
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
}

values = {
    "A":"Ace",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten",
    "J":"Jack",
    "Q":"Queen",
    "K":"King",
}

users = [
    "_user1",
    "_pgqgcycj",
    "_ajsnsjsk",
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
            img = "img/cards/%s%s.png"%(value, suit)
            write_card_md(path, img, values[value], suits[suit])

    # Generate Joker
    path = "%s/JO.md"%(base_dir)
    img = "img/cards/JO.png"
    write_card_md(path, img, "Joker", "")

