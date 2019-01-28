#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, io
reload(sys)
sys.setdefaultencoding("utf-8")

questions = []

LINE = 80

def jsonClean(text):
    return text.replace("\"", "\\\"").strip()

def breakPrompt(text):
    words = text.split(" ")
    out = ""
    leng = 0
    for word in words:
        if leng > LINE:
            out += "\n" + word + " "
            leng = 0
        else:
            out += word + " "
            leng += len(word)
    return out

with io.open("pytania.txt", "r", encoding="utf-8") as f:
    line = 0
    content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    while line < len(content):
        questionPrompt = jsonClean(content[line])
        line += 1
        if content[line].strip() != "":
            print "line " + str(line) + " should be empty"
            sys.exit(1)
        line += 1
        options = []
        trueAnswers = 0
        while content[line].strip() != "":
            try:
                cleanLine = jsonClean(content[line])
                if content[line].strip()[-1] == "x":
                    options.append((cleanLine[:-1], True))
                    trueAnswers += 1
                else:
                    options.append((cleanLine, False))
            except Exception as e:
                print "failed (" + str(line) + "): " + content[line] + str(e)
                sys.exit(1)
            line += 1
        """
        if trueAnswers == 0:
            print "line " + str(line) + ": no correct answers"
            sys.exit(1)
        """
        if line < len(content) and content[line].strip() != "":
            print "line " + str(line) + " should be empty"
            sys.exit(1)
        line += 1  # skip ---
        questions.append({
            "prompt": questionPrompt,
            "options": options,
        })

with io.open("src/app/pytania.ts", "w", encoding="utf-8") as f:
    f.write(unicode("export default class Questions { public static QUESTIONS = " + json.dumps(questions, indent=4).decode("unicode-escape")+";}"))