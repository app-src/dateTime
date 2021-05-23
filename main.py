import time, pyautogui
def main():
    n= int(input('Enter the no. of times you want to refresh: '))
    cnfm=input('{}{}{}'.format('You entered ',n,'. Hit enter to continue'))
    for i in range(n):
        pyautogui.click(1200,0,button='Right')

        #time.sleep(.1)

        pyautogui.click(1260,80)

        


main()        
