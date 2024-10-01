def makeGame():
    game = {
      "Start": ["You come across a fork at the road.", "Go right", "Right", "Go left", "Left"], 
      "Right": ["You failed to see a trap on the road.", "Start over", "Start over", "quit", "quit"], 
      "Left": ["While walking, you see a treasure chest", "Open the chest", "open", "leave it be", "leave"], 
      "Leave": ["As you continue to walk, you see a man walking your way.", "Approach him", "approach", "Ignore him", "Ignore"], 
      "open": ["You open the chest and get poisoned by mustard gas", "Start over", "Start over", "quit", "quit"], 
      "Ignore": ["You start walking away, the man gets angry and stabes you in the back", "Start over", "Start over", "quit", "quit"], 
      "Approach": ["He offers to give you one of two things from his pack.", "a mysterious potion", "potion", "A shiny sword", "sword"], 
      "mysterious potion": ["You drank the potion instantly and spontaniously combusted", "Start over", "Start over", "quit", "quit"], 
      "Sword": ["As you continue, you come across a few slow goblins", "Fight them", "Fight", "Run away", "Run"], 
      "Fight": ["As you fight them off a bigger goblin shows up and cuts you in half", "Start over", "Start over", "quit", "quit"], 
      "Run away": ["You finally find yourself back home after so long. YOU WIN!", "Start over", "Start Over", "quit", "quit"], 
      }
    return game

def playNode (game, node):
    currentNode = game[node]
    (description, menu1, node1, menu2, node2) = currentNode
    print (f"""
    {description}
        1. {menu1}
        2. {menu2}
    """)
    choice = input ("which will you do? (1/2)? ")
    if choice == "1":
        nextNode = node1
    elif choice == "2":
        nextNode = node2
    else:
        print("plese chose 1 or 2")
        nextNode = node
        
    return nextNode

def main():
    game = makeGame()
    keepGoing = True
    currentNode = "Start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game,currentNode)
main() 
