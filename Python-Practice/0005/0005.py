# -*- coding:utf-8 -*-
'''
0005: 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
'''
import os, re


def countLines(filename):
    totalLine, commentLine, blankLine = 0, 0, 0
    with open(filename, "rb") as f:
        lines = f.readlines()
        totalLine = len(lines)

        lineIndex = 0
        while lineIndex < totalLine:
            line = lines[lineIndex]
            if line.startswith("#"):
                commentLine += 1
            elif re.match("\s*'''", line) is not None and re.match(".+'''\\r\\n$", line) is not None:
                commentLine += 1
            elif re.match("\s*'''", line) is not None:
                commentLine += 1
                lineIndex += 1
                line = lines[lineIndex]

                while re.match(".*'''\\r\\n$", line) is None and lineIndex < totalLine - 1:
                    commentLine += 1
                    lineIndex += 1
                    line = lines[lineIndex]
                commentLine += 1

            elif line == "\n" or line == "\t":
                blankLine += 1
            lineIndex += 1
    return totalLine, commentLine, blankLine


def getFileLineCount(dir):
    os.chdir(dir)

    totalLine, commentLine, blankLine = 0, 0, 0

    for filename in os.listdir(os.getcwd()):
        if os.path.splitext(filename)[1] == '.py':
            fileLineCount = countLines(filename)
            totalLine += fileLineCount[0]
            commentLine += fileLineCount[1]
            blankLine += fileLineCount[2]

    print "totalLine: ", totalLine
    print "commentLine: ", commentLine, "  %0.2f%%" % (commentLine * 100.0 / totalLine)
    print "blankLine: ", blankLine, "  %0.2f%%" % (blankLine * 100.0 / totalLine)


if __name__ == '__main__':
    getFileLineCount(".")
