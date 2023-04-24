import pyautogui, time
import random

formData = [{'weight':str(225)},
{'weight':str(random.randint(85, 400))}]

pyautogui.PAUSE = .5
print('Ensure that the browser window is active and the form is loaded')
# https://autbor.com/form

for person in formData:
    #give the user a chance to kill the script
    print(' 5 second pause to let user press Ctrl-C or to click on the browser to make the browser active ')
    time.sleep(5)
    pyautogui.write(['\t','\t','\t', '\t','\t']) # needs five tabs not two to get to weight field field

    # Fill out the weight field.
    pyautogui.write(person['weight'] + '\t' + '\t') # writes the weight field and tabs to the calculate button

    # Press calculate
    pyautogui.write(['enter'])
   

    pyautogui.write(['\t', '\t', '\t'])# tabs 6 times to get back to the starting point