import uuid
from datetime import date


# GLOBAL VARIABLES

notes = [{"id": 'f73cc840-0118-41d1-85fe-602517cd1d24', "name": "Getting a burger", "date": 20211301}]
archive = []

new_note = str()
old_uuid = str()

today = 20210213
#today = datetime.today().strftime('%Y%m%d')


# FUNCTIONS

def CreateNote(new_note):
    new_dict = {"id": str(uuid.uuid1()),
                "name": new_note,
                "date": today,
                }
    notes.append(new_dict)
    print('Tasks to complete: ' + str(len(notes)))
    return print(notes)


def ArchiveNote(old_uuid):
    for i in range(len(notes)):
        if notes[i]['id'] == old_uuid:
            archive.append(notes[i])
            del notes[i]
            break
    print('Remaining tasks: ' + str(len(notes)))
    return print(notes)


# EXECUTION

CreateNote('Doing the dishes')
print('Tasks to complete: ' + str(len(notes)))
print(notes)

ArchiveNote("f73cc840-0118-41d1-85fe-602517cd1d24")
print('Task has been archived: ')
print(archive)