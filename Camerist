# -*- coding: UTF-8 -*-
import os
import sys
import traceback
import shutil
from easygui import *

softVersion = 'Версия программы - 0.0.8'

class scanDir:
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
                print y.encode('utf-8') #Для теста
                shutil.copy(fromCopy+'\\'+y,new_path)
        except :
            exceptionbox()
        else:
            msgbox(msg= new_path, title = 'Файлы перемещены в ' )

    # Перемещаем файлы
    # fileList - Список файлов которые надо копировать
    # fromCopy - Откуда копируем файлы
    # new_path - Куда перемещаем файлы
    def moveFile(self,fileList,fromCopy,new_path):
        try:
            for y in fileList:
                print y
                shutil.move(fromCopy+'\\'+y,new_path)
        except :
            exceptionbox()
        else:
            msgbox(msg= new_path, title = 'Файлы перемещены в ' )
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
                        if creatrPathDst == None:
                            break
                        # Скануируем папку для получение список файлов.
                        pathScan = diropenbox(msg ='Скануируем папку для получение список файлов (Обработанные файлы)')
                        if pathScan == None:
                            break
                        # Откуда копируем
                        fromCopy = diropenbox(msg ='Откуда копируем файлы (Оригинальные файлы)')
                        if fromCopy == None:
                            break
                        #Запуск процесса
                        if ynbox(msg='Запустить процесс?',choices=('[<F1>]Yes', '[<F2>]No')):
                            s=scanDir()
                            fileScan = s.scanDirOnlyFile(pathScan)
                            newFolder = s.createrFolder(creatrPathDst,nameFolder)
                            copyFile = s.copyFile(fileScan,fromCopy,newFolder)
                    except :
                        exceptionbox ()
                    break
        elif reply == "2":
            textbox(msg=softVersion, title='В помощь фотографу', text='', codebox=0)

main()
