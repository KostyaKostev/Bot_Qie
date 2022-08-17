import os
import sys


def match(el1, el2):
    incorrect_symbols = 0
    if len(el2) > len(el1):
        while len(el2) > len(el1):
            el1 += '_'
    for i in range(len(el2)):
        if el1[i] != el2[i]:
            incorrect_symbols += 1
    if incorrect_symbols > 3:
        return False
    else:
        return True


class Qie_Bot:
    def __init__(self, commands_file):
        file = open(commands_file, 'r')
        self.commands_list = []
        self.not_working = False
        for line in file:
            self.commands_list.append(line[:-1])

    def add_file(self, filename, path):
        pass

    def delete_file(self, filename, path):
        pass

    def add_folder(self, foldername, path):
        pass

    def delete_folder(self, foldername, path):
        pass

    def add_file_in_folder(self, foldername, filename, path1, path2):
        pass

    def delete_file_in_folder(self, foldername, filename, path1, path2):
        pass

    def shut_process(self, processname):
        pass

    def exit_qie(self):
        self.not_working = True

    def cmd_open(self):
        pass

    def command_recognition(self, command):
        for element in self.commands_list:
            if match(element, command):
                self.current_command = command