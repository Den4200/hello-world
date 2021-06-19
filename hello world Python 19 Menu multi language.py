# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:46:08 2020

@author: TechnoVixen-Natani
"""
# My attempt at making Hello World with the most common language per
# continent based on wiki article 
# Please note that some translations do not have
# acent symbols per the correct spelling
# I am still trying to figure this out
# https://en.wikipedia.org/wiki/List_of_languages_by_the_number_of_countries_in_which_they_are_recognized_as_an_official_language

menu_prompt = ("1.English\n"
               "2.Arabic\n"
               "3.French\n"
               "4.German\n"
               "5.Portuguese\n"
               "6.Italian\n"
               "7.Russian\n"
               "8.Dutch\n"
               "9.Swahili\n"
               "10.Chinese\n"
               "11.Serbo-Croatian\n"
               "12.Malay\n"
               "13.Swedish\n"
               "14.Albanian\n"
               "15.Polish\n"
               "16.Sotho\n"
               "17.Czech\n"
               "18.Hindi\n"
               "19.Exit\n")

while True: # Exit if no input entered
    command = input(menu_prompt).lower().strip()
    if command == '1':
        print('Hello World!')
    elif command == '2':
        print('marhabaan bialealam')
    elif command == '3':
        print('Bonjour le monde')
    elif command == '4':
        print('Hallo Welt')
    elif command == '5':
        print('Olá Mundo')
    elif command == '6':
        print('Ciao mondo')
    elif command == '7':
        print('Privet mir')
    elif command == '8':
        print('Hallo Wereld')
    elif command == '9':
        print('Salamu, Dunia')
    elif command == '10':
        print('Niǐ hao, shijie')
    elif command == '11':
        print('Pozdrav svijete')
    elif command == '12':
        print('Hai dunia')
    elif command == '13':
        print('Hej varlden')
    elif command == '14':
        print('pershendetje Bote')
    elif command == '15':
        print('Witaj swiecie') 
    elif command == '16':
        print('lefatse Lumela')
    elif command == '17':
        print('Ahoj svete')
    elif command == '18':
        print('Namaste duniya')
    elif command == '19':
        break
    else:
        print('Command not recognized,'
              'please check the number and dial again')