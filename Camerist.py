# -*- coding: utf-8 -*-
import os
import sys
#import traceback
import shutil
from easygui import *

softVersion = 'Версия программы - 0.1.1'

class scanDir:
    # Новый метод возвращает только список файлов
    # Данный метод взят с сайта http://stackoverflow.com/questions/11968976/python-list-files-in-the-current-directory-only
    # pathScan - Где сканировать
    # fileList - Возвращает список фалов
    def scanDirOnlyFile(self,pathScan):
        fileList = [ f for f in os.listdir(pathScan)if os.path.isfile(os.path.join(pathScan,f))]
        return fileList

    # Создаем новую папку
    # creatrPathDst - путь где будет создана новая папка
    # nameFolder - Наименование новой папки
    def createrFolder(self,creatrPathDst,nameFolder):
        try:
            new_path = creatrPathDst +'\%s' % (nameFolder)
            os.makedirs(new_path)
        except :
            exceptionbox()
        return new_path


    # Копируем файлы
    # fileList - Список файлов которые надо копировать
    # fromCopy - Откуда копируем файлы
    # new_path - Куда копируем файлы
    def copyFile(self,fileList,fromCopy,new_path):
        try:
            for y in fileList:
                print y
                shutil.copy(fromCopy+'\\'+y,new_path)
        except :
            exceptionbox()
        else:
            msgbox(msg= new_path, title = 'Файлы перемещены в ' )

#Функция обрезает и изменения формата для копирования.
##def pop(filelist):
##    namesFile = []
##    newFiles = []
##    for x in filelist:
##        namesFile.append(x[:-4]) # для .JPG нужно ставить '-4' # для .JEPG нужно ставить '-5'
##    for y in namesFile:
##        newFiles.append(y+'.NEF') # Зависит от формата "фотика"
##    return newFiles

# Функция немного переписаны, но суть осталась не изменна. Теперь не надо ставить цифры '-4' или '-5' для форматов jpeg и jpg
def pop(filelist):
    namesFile = []
    newFiles = []
    for x in filelist:
        namesFile.append(x.rstrip('.jpg') and x.rstrip('.jpeg'))
    for y in namesFile:
        newFiles.append(y+'.NEF') # Зависит от формата фотоаппарата. Этот формат "Nikon"
    return newFiles

def main():
    while True:
        msg = ""
        title = "В помощь фотографу"
        choices = ["1 - Копирование, пермещение и создание новой папки","2 - О программе",]
        choice = choicebox(msg, title, choices)
        if not choice: return
        reply = choice.split()[0]
        if reply == "1":
            while True:
                nameFolder = enterbox(msg=u'Введите имя папки')
                if nameFolder == '':
                    msgbox(u'Вы не ввели имя папки!')
                elif nameFolder == None:
                    break
                else:
                    try:
                        # Где создать папку
                        creatrPathDst = diropenbox(msg ='Где создать папку?')
                        
                        # Скануируем папку для получение список файлов.
                        pathScan = diropenbox(msg ='Скануируем папку для получение список файлов (Оригинальные файлы)')

                        # Откуда копируем
                        fromCopy = diropenbox(msg ='Откуда копируем файлы (Обработанные файлы)')
                        #
                        if ynbox(msg='Запустить процесс?',choices=('[<F1>]Yes', '[<F2>]No')):
                            s=scanDir()
                            fileScan = s.scanDirOnlyFile(pathScan)
                            newFolder = s.createrFolder(creatrPathDst,nameFolder)
                            copyFile = s.copyFile(pop(fileScan),fromCopy,newFolder)
                            #msgbox(msg=copyFile,title = 'Имена файлов')
                    except :
                        exceptionbox ()
                    break
        elif reply == "2":
            textbox(msg=softVersion, title='В помощь фотографу', text='', codebox=0)

main()
