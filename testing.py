# coding: latin-1
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#new point to add... make rest of function then compare a list of monuments notaries ( such as blvd, road, street, etc.) to a list of words containing them. if contained, pass into new set ( ref notes in case) 


def regex(url):
   
  html = urlopen(url).read()    
  soup = BeautifulSoup(html,"lxml") # why does lmxl fix it?
  sets = []
  
  john = [u'Julia Alvarez', u'Arambilet',  u'Frank Baez',u'Josefina Baez' u'Rei Berroa',u'Manuel del Cabral', u'Junot Díaz', u'Luis Arambilet' u'Manuel del Cabral', u'Manuel del Cabral' u'Aída Cartagena Portalatín', u'Roberto Cassá', 'Raquel Cepeda',u'Tulio Manuel Cestero',u'Hilma Contreras', u'Angie Cruz', u'Judith Dupré',u'Virginia Elena Ortea',u'León Félix Batista', u'Arturo Féliz-Camilo',u'Fabio Fiallo',u'Freddy Ginebra',u'Cristino Gómez',u'José Luis González',u'Pedro Henríquez Ureña',u'Federico Henríquez y Carvajal',u'Angela Hernández Nuñez',u'Juan Isidro Jiménez Grullón',u'Rita Indiana',u'Mariano Lebrón Saviñón',u'Marcio Veloz Maggiolo',u'Andrés L. Mateo', u'Félix Evaristo Mejía',u'Miguel D. Mena',u'Leopoldo Minaya', u'Juan Duarte',u'Rafael Alburquerque',u'Pedro Franco Badía ',u'Buenaventura Báez Méndez',u'Joaquín Balaguer Ricardo',u'Ramón Emeterio Betances',u'Salvador Jorge Blanco',u'Tomás Bobadilla',u'Juan Bosch y Gaviño',u'Francisco Alberto Caamaño Deñó',u'Fernando Cabrera',u'Ramón Cáceres',u'Margarita Cedeño de Fernández',u'David Collado', u'Lorraine Cortés-Vázquez',u'Adriano Espaillat',u'Juan Pablo Duarte',u'Rafael Espinal',u'Rafael Estrella Ureña',u'Carlos Felipe Morales', u'Leonel Fernández Reyna',u'Pedro Florentino',u'Maximiliano Gómez',u'Máximo Gómez',u'Petronila Angélica Gómez',u'Antonio Guzmán Fernández',u'Ulises Heureaux',u'Antonio Imbert Barrera',u'Gregorio Luperón',u'Miguel Martinez',u'Danilo Medina',u'Hipólito Mejía',u'Ramón Matías Mella',u'Patria Mirabal',u'Minerva Mirabal',u'María Teresa Mirabal',u'Adolfo Alejandro Nouel',u'José Nuñez-Melo',u'José Francisco Peña Gómez', u'Joseline Peña-Melnyk',u'Cesar A. Perales',u'Thomas Perez',u'Donald Reid Cabral',u'Ydanis Rodríguez',u'José Antonio Salcedo',u'Pepillo',u'Roberto Salcedo, Sr.',u'Juan Sánchez Ramírez',u'Francisco del Rosario Sánchez',u'José Santana', u'Pedro Santana Familias',u'José Del Castillo Saviñón',u'Angel Taveras', u'Rafael Leónidas Trujillo',u'Ramfis Trujillo',u'Francisco Urena',u'Fernando Valerio', u'Elias Wessin y Wessin blvd', u'Salome Urena de Henriquez']

  jake = [u'Pedro Mir',u'Domingo Moreno Jimenes',u'Mateo Morrison',u'José Núñez de Cáceres',u'Arturo Rodríguez Fernández',u'Mu-Kien Adriana Sang',u'Rosa Silverio',u'Alfredo Fernández Simó',u'Salomé Ureña',u'Jael Uribe',u'Bernardo Vega',u'Julio Vega Batlle',u'Alanna Lockward',u'Delia Weber', u'statue'] #list of words , only set


  

  paul = jake + john

  new_list = [x.encode('latin-1') for x in sorted(paul)]

  search = "(" + b"|".join(new_list).decode() + ")" + "" #re.complie needs string as first argument, so adds string to be first argument, and joins the strings together with john

 # print (type(search))
  pattern = re.compile(search)#compiles search to be a regex object
  reg = pattern.findall(str(soup))#calls findall on pattern, which findall returns all non-overllapping matches of the pattern in string, returning a list of strings

  for i in reg:
     if i in paul: # this loop checks to see if elements are in both the regexed parsed list and the list. If i is in both, it is added to list. 
            sets.append(str(i))
  return sets
                


def regexparse(regex):
    monum = [u'road',u'street', u'town', u'city', u'blvd', u'terrace', u'ave', u'avenue', u'park',u'lane', u'school', u'monument', u'statue']
    setss = []
    
    f = regex
    f = list(f)
    for i in f:
       if i in monum:
              setss.append(i)
              with open ('regex.txt','w') as q:
                  q.write(str(setss))
               
    print (setss)


if __name__ == '__main__':
   regexparse(regex('https://www.tripadvisor.com/Attractions-g147288-Activities-c47-t26-Dominican_Republic.html'))
