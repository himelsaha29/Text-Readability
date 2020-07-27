# author :: HimelSaha


text = input("Text: ")                                          # input text from user

letterCount = 0
spaceCount = 0
sentenceCount = 0

for i in range(0, len(text)):

    if (text[i] == '.' or text[i] == '!' or text[i] == '?'):    # if iteration encounters these characters, increase sentence counter by 1

        sentenceCount += 1

    elif (text[i] >= 'A' and text[i] <= 'Z'):                   # if iteration encounters these characters, increase letter counter by 1

        letterCount += 1

    elif (text[i] >= 'a' and text[i] <= 'z'):                   # if iteration encounters these characters, increase letter counter by 1

        letterCount += 1

    elif (text[i] == ' '):                                      # if iteration encounters these characters, increase space counter by 1

        spaceCount += 1

    else:                                                       # otherwise skip iteration

        continue



wordCount = spaceCount + 1                                      # wordCount is 1 more than space count

first = (100 * (letterCount / wordCount))                       #  the average number of letters per 100 words in the input text
second = (100 * (sentenceCount / wordCount))                    #  the average number of sentences per 100 words in the input text


index = round((0.0588 * first) - (0.296 * second) - 15.8)       # calculated readability

if (index >= 16):

    print("Grade 16+\n")

elif (index < 1):

    print("Before Grade 1\n")

else:

    print("Grade", index)