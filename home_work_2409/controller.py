import gui
import actions

def work():
    p = gui.path_file()
    act = gui.action()
    match act:
        case 'read':
            actions.read_file(p)
        case 'write':
            actions.write_in_file(p)
        case 'find':
            actions.find_in_file(p)
        case 'delete':
            actions.delete_in_file(p)