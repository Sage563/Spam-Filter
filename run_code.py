def scream():
    text = "RUN THIS CODE!!!"
    big_text = "\n".join([" ".join(text) for _ in range(3)])
    print("\033[1;31m" + big_text + "\033[0m")

scream()
