from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class JokesAboutFinnishPeople(MycroftSkill):
    def __init__(self):
       super().__init__()
        self.learning = True

    @intent_handler('people.finnish.about.jokes.intent')
    def handle_people_finnish_about_jokes_intent(self, message):
        self.speak_dialog('people.finnish.about.jokes')

    def stop(self):
        pass


def create_skill():
    return JokesAboutFinnishPeople()
