 # Python Mad Libs Warm-Up Activity

   # Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")

   # Gather user inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

   # Build the story using an f-string
story = (
       f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
       "I couldn't believe my eyes!"
   )

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
   