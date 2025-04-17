import comments
from model import Model
import strip
import score
import mids
inputs =input("Enter the url(or 'exit' to quit): ")
if inputs == 'exit' or inputs == 'quit':
    print("Exiting the program.")
    exit(0)

if type(inputs) != str:
    print("Invalid input. Please enter a valid URL.")

inpute =int(input("Enter the number of comments to fetch"))

comments_instance =comments.Comment(f"{strip.strip_youtube_url(inputs)}",inpute).run()
mymodel = Model()
mymodel.run()


print("\n----------------------------------\n")


stat =input("Do you want to display the results? (yes/no):")
if stat =="yes":
    scorenum =mymodel.display_results()
    print(scorenum)
elif stat == "no":
    print("Results not displayed.")


print("\n----------------------------------\n")

stit =input("Do you want the overal score? (yes/no):")

if stit == "yes":
    score_instance = score.LoadDict_score()
    scores = score_instance.run()
    rating = score_instance.rating()
    print(f"Overall Score: {scores}")
    print(f"Rating of the comments: {rating}")
elif stit == "no":
    print("Score not displayed.")

print("\n----------------------------------\n")

do_you = input("Do you want to check for spam comments? (yes/no): ")


if do_you.lower() == "yes":
    spam_detector = mids.SpamDetector()
    spam_results = spam_detector.run()
    print("Spam Detection Results:")
    print(spam_results)
elif do_you.lower() == "no":
    print("Spam detection skipped.")

do_so = input("Do you want all comments? (yes/no): ")
if do_so.lower() == "yes":
    print(open("fullresults.json", "r", encoding="utf-8").read())