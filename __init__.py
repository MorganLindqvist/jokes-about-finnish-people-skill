from mycroft import MycroftSkill, intent_file_handler


class JokesAboutFinnishPeople(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('people.finnish.about.jokes.intent')
    def handle_people_finnish_about_jokes(self, message):
        self.speak_dialog('people.finnish.about.jokes')


def create_skill():
    return JokesAboutFinnishPeople()

