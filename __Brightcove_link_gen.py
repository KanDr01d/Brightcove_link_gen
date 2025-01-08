import art, os, time, http, urllib.request, os.path
from time import sleep
from os import name
from art import *


def clear():
    # Windows
    if name == "nt":
        _ = os.system("cls")

    # Linux, Unix & Mac
    else:
        _ = os.system("clear")


def wait_for_press():
    # Windows
    if name == "nt":
        _ = os.system("pause")

    # Linux, Unix & Mac
    else:
        _ = os.system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
        print()


def LinkCheck(link):
    if urllib.request.urlopen(link).getcode() != 200:
        exit(1)
    else:
        return 0


def LinkGen():
    clear()
    Account_ID = input("Enter Account ID: ")
    Player_ID = input("Enter Player ID: ")
    Video_ID = input("Enter Video ID: ")
    Final_Link = ("https://players.brightcove.net/" + Account_ID + "/" + Player_ID + "_default/index.html?videoId=" + Video_ID)
    LinkCheck(Final_Link)
    print("Final link: ", Final_Link)
    exit(0)


def GenHelp():
    print("Q: Where can i find Account ID, Player ID, Video ID?")
    print(
        'A: Right click and select "Player Information". You can see all of the needed data here'
    )
    wait_for_press()
    Menu()


def Menu():
    clear()
    global MenuOpt
    tprint("Brightcode   link   generator\n\n")
    print("1. Link generator")
    print("2. Help")
    print("3. Exit\n")
    MenuOpt = int(input(">> "))
    if MenuOpt == 1:
        LinkGen()
    elif MenuOpt == 2:
        GenHelp()
    elif MenuOpt == 3:
        exit(0)
    else:
        print("Syntax Error: Not known option")
        sleep(2)
        clear()
        Menu()


Menu()
