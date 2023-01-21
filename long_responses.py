import random

R_ADVICE = "If you are interested,I would suggest this college is the best option."


def unknown():
    response = ["Could you please re-phrase that? ",
                "What does that mean?"][
        random.randrange(2)]
    return response