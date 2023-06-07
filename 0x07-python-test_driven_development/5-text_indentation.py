#!/usr/bin/python3
""" divide matrix module """


def text_indentation(text):
    """
       new line after evry ? . or :
       args:
           text (str): text to change
       return:
           None
     """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    changed = False

    for i in text:
        if ":?.".find(i) != -1:
            new_text += "\n\n"
            changed = True
        elif i == " " and changed:
            continue
        else:
            new_text += i
            changed = False
    print(new_text)
