# Exercício 9.7
def getFilename(path):
    filename = path.split('/')[-1]
    return filename

# Exercício 9.14
def removeSpaces(string=''):
    spaces = 0
    newString = ''
    for char in string:
        if char != ' ':
            newString += char
            spaces = 0
        else:
            if spaces < 1:
                newString += char
                spaces += 1
    return newString

def removeEmptyLine(content=''):
    emptyLine = 0
    newString = ''
    for line in content:
        if line != '\n':
            newString += line
            emptyLine = 0
        else:
            if emptyLine < 1:
                newString += line
                emptyLine += 1
    return newString
