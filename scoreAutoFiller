import pyautogui, time
import random

formData = [{'bodyWeight':str(220), 'total': str(1600)},
{'bodyWeight':str(235), 'total': str(1500)},
{'bodyWeight':str(185), 'total': str(1333)},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))},
{'bodyWeight':str(random.randint(85, 400)), 'total': str(random.randint(135, 2610))}]

pyautogui.PAUSE = .5
print('Ensure that the browser window is active and the form is loaded')
# https://autbor.com/form

for person in formData:
    #give the user a chance to kill the script
    print(' 5 second pause to let user press Ctrl-C or to click on the browser to make the browser active ')
    time.sleep(5)
    pyautogui.write(['\t','\t','\t', '\t','\t'])

    # Fill out the Bodyweight field.
    pyautogui.write(person['bodyWeight'] + '\t')

    # Fill out the Total field.
    pyautogui.write(person['total'])

    pyautogui.write(['\t','\t','\t'])