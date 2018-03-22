# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import re

def switch_dia(argument):
	return {
        '2': "Segunda-Feira",
        '3': "Terca-Feira",
        '4': "Quarta-Feira",
        '5': "Quinta-Feira",
        '6': "Sexta-Feira",
        '7': "Sabado"
    }[argument]


def print_JSON(dia, periodo, aula, professor, ):
	
	json=('"dia":"{0}","periodo":"{1}","aula":"{2}","professor":"{3}"'.format(dia,periodo,aula,professor))
	print("{"+json+"}")

file = open("/home/suporte/Downloads/E105.html","r")
html = file.read()
soup = BeautifulSoup(html)
dias = re.findall("dv.*[a-z][0-7]",html)
for linha in soup.findAll('td',{'id':dias}):
	#print str(linha)
	aulas = re.search("\">[A-Z](.*?)<",str(linha))
	professor = re.search("<br \/>[A.-Z ]+<br \/>",str(linha))
	if(aulas!=None):
		diaCompleto = re.search("dv.*[a-z][0-7]",str(linha)).group()
		dia = switch_dia(diaCompleto[3])
		periodo =diaCompleto[4:]
		print_JSON(dia,periodo,aulas.group()[2:-1],professor.group()[6:-6])

		# print dia
		# print periodo
		# print "Aula:"
		# print aulas.group()[2:-1]
		# print "Professor:"
		# print professor.group()[6:-6]
