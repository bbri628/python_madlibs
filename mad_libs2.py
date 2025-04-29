# Python Mad Libs Challenge 2

import random

def play_mad_libs():
    # Welcome message
    print("Welcome to Python Mad Libs!")
    print("Answer the following questions to create your very own silly story.\n")

    # Gather user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # List of story templates (note: no f-strings here)
    templates = [
        "Today, I saw a {adjective} {noun} that decided to {verb} {adverb}. I couldn't believe my eyes!",
        "The {adjective} {noun} likes to {verb} {adverb} every morning before breakfast.",
        "Once upon a time, a {noun} who was very {adjective} tried to {verb} {adverb} across the kingdom.",
        "In a {adjective} forest, a {noun} suddenly began to {verb} {adverb}."
    ]

    # Choose a random story and fill in the placeholders
    story_template = random.choice(templates)
    story = story_template.format(adjective=adjective, noun=noun, verb=verb, adverb=adverb)

    # Display the completed story
    print("\nHere is your story:")
    print(story)
# Replay loop
while True:
    play_mad_libs()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye!")
        break