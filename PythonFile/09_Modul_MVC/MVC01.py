from Model import Person
import view

def showAll():
    people_in_db = Person.getAll()
    return view.showAllView(people_in_db)
def start():
    view.startView()
    #input = raw_input()
    if input == 'y':
        return showAll()
    else:
        return view.endView()


if __name__ == "__main__":
    start()