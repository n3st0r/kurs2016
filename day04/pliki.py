#!/usr/bin/env python


plik = 'test.txt'

file = open(plik, 'r', encoding='UTF')
zawartosc = file.readlines()
# print(zawartosc)

for index,linia in enumerate(zawartosc):
    print (index, ': ', linia, ' a jej dlugość: ', len(linia))

# with open(plik, 'r') as infile:
#     for line in infile:
#         print(line)
