import os


def handler(context, event):
    print(context)
    print(event)
    print(os.getenv("JUST_A_KEY"))
    return ""
