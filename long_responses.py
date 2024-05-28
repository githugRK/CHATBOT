import random

R_EATING = "I dont't like eating anything because I'm a ROBOT obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exatly that you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                ".......",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response