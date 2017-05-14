iNumber = 11
jNumber = 11
t = '\t'
s = ('').join('<!DOCTYPE HTML>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title>Multiplication table</title>'
              '\n\t\t<style>\n\t\t\ttable{\n\t\t\t\tborder-collapse: collapse;\n\t\t\t\tmargin: auto;\n\t\t\t}\n' 
              '\t\t\ttr, td, th{\n\t\t\t\tborder: 1px solid #333;\n\t\t\t\tborder-style:dashed;\n\t\t\t\tpadding: 3px;'
              '\n\t\t\t\tbackground: #E5FBE9;\n\t\t\t\ttext-align: center;\n\t\t\t}\n\t\t\tth {\n \t\t\t\tbackground:'
              ' #8BBBB0;\n\t\t\t\tborder-style:solid;\n\t\t\t}\n\t\t</style>\n \t</head>\n\t<body>\n    \t<table>\n'
              '    \t<caption>Multiplication table</caption>\n')

s += t * 3 + '<tr>\n' + t * 4
for i in range(jNumber):
    s += '<th>' + str(i) + '</th>'
s += '\n' + t * 3 + '</tr>\n'
for i in range(1, iNumber):
    s += t * 3 + '<tr>\n' + t * 4 + '<th>' + str(i) + '</th>'
    for j in range(1, jNumber):
        s += '<td>' + str(i * j) + '</td>'
    s += '\n' + t * 3 + '</tr>\n'
s += '\t\t</table>\n  \t</body>\n</html>\n'

file = open('Multiplication table.html', 'w')
file.write(s)
file.close()



