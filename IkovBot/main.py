import pyautogui

#Game screen starts at pixel...
first_game_px_x, first_game_px_y = 676, 82
last_game_px_x, last_game_px_y = 1193, 419

#The character is always on the center of the screen
character_pos_x = ((last_game_px_x - first_game_px_x) / 2 ) + first_game_px_x
character_pos_y = ((last_game_px_y - first_game_px_y) / 2 ) + first_game_px_y
#Runescape time tick 
rs_time_tick = 0.6
rs_time_safe_tick = rs_time_tick + 0.4

first_log_x, first_log_y = 1255, 310
log_space_x, log_space_y = 40, 35
drop_space_y = 75
second_log_row_space_y = 55
last_log_row_space_y = 20

def teleport_to_wc():
    #Where the TP book is
    tp_book_px_x, tp_book_px_y = 1425, 265
    #Skill to tp
    tp_px_x, tp_px_y = 1294, 415
    pyautogui.click(tp_book_px_x, tp_book_px_y)
    pyautogui.sleep(rs_time_safe_tick)
    pyautogui.click(tp_px_x, tp_px_y)
    pyautogui.sleep(rs_time_safe_tick)
    pyautogui.keyDown("C")
    pyautogui.keyUp("C")
    pyautogui.sleep(rs_time_safe_tick)
    pyautogui.keyDown("A")
    pyautogui.keyUp("A")
    return True

def center_screen():
    center_btn_x, center_btn_y = 1218, 104
    pyautogui.click(center_btn_x, center_btn_y)
    pyautogui.keyDown("ArrowUp")
    pyautogui.sleep(1.5)
    pyautogui.keyUp("ArrowUp")
    return True

def chopTillFullInv(inv_space):
    #Chop, if the log appear on the bag, than chop again, 28 times
    if inv_space == 0:
        return
    return chopTillFullInv(inv_space - 1)

def dropTillEmptyInv(inv_space, log_x = first_log_x, log_y = first_log_y, log_n = 0):
    pyautogui.rightClick(log_x, log_y)
    pyautogui.sleep(rs_time_tick / 2)
    if log_n >= 20 and log_n < 24:
        pyautogui.click(log_x, log_y + second_log_row_space_y)
    elif log_n >= 24:
        pyautogui.click(log_x, log_y + last_log_row_space_y)
    else:
        pyautogui.click(log_x, log_y + drop_space_y)
    pyautogui.sleep(rs_time_tick / 2)

    log_x += log_space_x
    log_n += 1

    if log_n % 4 == 0:
        log_x = first_log_x
        log_y += log_space_y
    
    if inv_space == 0:
        print("Inventory is empty")
        return True
    return dropTillEmptyInv(inv_space - 1, log_x, log_y, log_n)


def main():
    print("Starting....")
    pyautogui.sleep(2)
    if dropTillEmptyInv(27):
        print("Inventory is empty")

    # while True:
    #     #Safe time after starting to click on IKOV SCREEN
    #     print("Starting....")
    #     pyautogui.sleep(2)
    #     #Teleport to WC Location
    #     teleport_to_wc()
    #     chopTillFullInv(28)
    #     dropTillEmptyInv(28)
    #Search for trees
    #Start chopping trees
    #Drop or deposit logs


if __name__ == "__main__":
    main()

