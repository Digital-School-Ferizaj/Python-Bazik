from tkinter import Tk, simpledialog, messagebox

def get_events():
    list_events = []
    with open("uefa_euro_results.txt") as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split('/')
            list_events.append(current_event)
    return list_events

def write_to_file(year, countries, score):
    with open("uefa_euro_results.txt", "a") as file:
        file.write('\n' + year + '/' + countries + '/' + score)

root = Tk()
root.withdraw()

events = get_events()

query_year = simpledialog.askstring('Year', 'Type the year:')

knowAnswer = False

for event in events:
    event_year = event[0]
    if query_year == event_year:
        knowAnswer = True
        countries = event[1]
        score = event[2]
        messagebox.showinfo('Answer', 'The score of euro '+ event_year + ' was ' + countries + " : " + score)
        break

if knowAnswer == False:
    new_countries = simpledialog.askstring("Teach me", "I don't know! Who were the finalsits in euro "+ query_year+"?")
    new_score = simpledialog.askstring("Score", "what was the score?")
    write_to_file(query_year, new_countries, new_score)
    




        
