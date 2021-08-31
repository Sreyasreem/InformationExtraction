import urllib.request, urllib.error, urllib.parse
import re
from ply.lex import lex
from ply.yacc import  yacc

#movie info
result = {}

#director list
director = []

#writer list
writer = []

#producer list
producer = []

#real name of actors
actual_name = []

#movie name of actors
movie_name = []

#dictionary of the genre
films = {
  "action_adventure": "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/",
  "animation": "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/",
  "drama": "https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/",
  "comedy": "https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/",
  "mystery_suspense": "https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/",
  "horror": "https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/",
  "science_fiction_fantasy": "https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/",
  "documentary": "https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/",
  "romance": "https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/",
  "classics": "https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/"
}



# tokens list
tokens = (
	'LMOVIE', 
    'BOXOFFICE',
	'LLANGUAGE',
    'LSTORY', 
	'RUNTIME',
     'LDIR', 'CELEBRITY', 
     'separator', 'ACTUALNAME', 'CHARNAME'	
    )


#MOVIENAME
def t_LMOVIE(t):
    r'<h1\sslot="title"\sclass="scoreboard__title"\sdata-qa="score-panel-movie-title">(.+)</h1>'
    t.value = t.lexer.lexmatch.groups()[1]
    
    return t    


#Box Office
def t_BOXOFFICE(t):
    r'<div\sclass="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Box\sOffice\s\(Gross\sUSA\):</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">(.+)</div>'
    t.value = t.lexer.lexmatch.groups()[3]
    
    return t

#Original Language
def t_LLANGUAGE(t):
    r'<div\sclass="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Original\sLanguage:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">(.+)'
    t.value = t.lexer.lexmatch.groups()[5]
    
    return t

#Run Time
def t_RUNTIME(t):
    r'<div\sclass="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Runtime:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">[\s\S]*?<time\sdatetime=".*">[\s\S]*?(.+)'
    t.value = t.lexer.lexmatch.groups()[7].strip()
   
    return t

#storyline
def t_LSTORY(t):

    r'<div\sid="movieSynopsis"\sclass="movie_synopsis\sclamp\sclamp-6\sjs-clamp"\sstyle="clear:both"\sdata-qa="movie-info-synopsis">[\s\S]*?(.+)'
    t.value = t.lexer.lexmatch.groups()[9].strip()
    
    return t

#director                   
def t_LDIR(t):

    r'<a\shref="/celebrity/.+"\sdata-qa="movie-info-director">(.+)</a>'
    t.value = t.lexer.lexmatch.groups()[11]
    
    return t

#celebrity
def t_CELEBRITY(t):
    r'<a\s+href="/celebrity/.+">(.+)</a>'  
    t.value = t.lexer.lexmatch.groups()[13]
    
    return t

#separator token
def t_separator(t):
    r'<div\sclass="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Writer:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">[^<]*?'
    
    return t


#real name of the actor
def t_ACTUALNAME(t):
    
    r'<a\shref="\s/celebrity/.*\s"\sclass="unstyled\sarticleLink"\sdata-qa="cast-crew-item-link">\n.*\n.*<span\stitle="(.*)">'
    t.value = t.lexer.lexmatch.groups()[16]
    
    return t

#movie name of the actor    
def t_CHARNAME (t):

    r'<span\sclass="characters\ssubtle\ssmaller"\stitle=".*">\n.*\n.*<br/>\n.*\n(.*)'
    t.value = t.lexer.lexmatch.groups()[18].strip()

    return t
 
        
# Error handling rule
def t_error(t):
    t.lexer.skip(1)


# Parsing Rules
def p_start(p):
	'''start : moviename storyline language director producer writer boxoffice runtime crew 
			 '''
	pass
    
def p_moviename(p):
    '''moviename : LMOVIE 
                 | epsilon '''

    
    if p[1]:
       result['Movie Name'] = p[1]
       
    else:
       result['Movie Name'] = 'N/A'

    pass

def p_storyline(p):
    '''storyline : LSTORY 
                 | epsilon '''

    if p[1]:
       result['Storyline'] = p[1]
       
    else:
       result['Storyline'] = 'N/A'

    pass

def p_language(p):
    '''language : LLANGUAGE 
                | epsilon '''
    
    if p[1]:
       result['Original Language'] = p[1]
       
    else:
       result['Original Language'] = 'N/A'

    pass
              
def p_director(p):
    '''director : director dval 
                | dval 
                | epsilon '''
                 
    pass


def p_dval(p):
    'dval : LDIR'
    
    if p[1]:
       director.append(p[1])

    pass    
   
def p_producer(p):
    '''producer : lprod producer 
                | lprod 
                | epsilon''' 
               
    pass           


def p_writer(p):
    '''writer : separator lwrite writer 
              | lwrite writer
              | lwrite 
              | epsilon '''

    pass

def p_lwrite(p):
    'lwrite : CELEBRITY'
    
    if p[1]:
       writer.append(p[1])

    pass 
 
def p_lprod(p):
    'lprod : CELEBRITY'

    if p[1]:
       producer.append(p[1])
    
    pass 
                     
def p_boxoffice(p):
    '''boxoffice : BOXOFFICE 
                 | epsilon '''
                 

    if p[1]:
       result['Box Office Collection'] = p[1]
       
    else:
       result['Box Office Collection'] = 'N/A'   

    pass
    
def p_runtime(p):
    '''runtime : RUNTIME 
               | epsilon '''

    if p[1]:
       result['Runtime'] = p[1] 
    
    else: 
       result['Runtime'] = 'N/A'  

    pass

def p_crew(p):
    '''crew : crew lcast
            | lcast
            | epsilon ''' 


    pass
    
def p_lcast(p):
    '''lcast : ACTUALNAME CHARNAME
             | ACTUALNAME epsilon
             | epsilon CHARNAME '''
    
    if p[1] and p[2]:
       actual_name.append(p[1]) 
       movie_name.append(p[2])  
   
    pass

def p_epsilon(p):
    'epsilon : '
    
    pass
                                    
def p_error(p):
    pass

def main():

   #html file of movie
   movie_file_list = []

   #dictionary of the urls of the 100 movies
   movie_dict = {}

   #user input movie name
   movie = None

   #file index
   index = 0

   #movie index
   count = 0
   
   
    
   for genre, url in films.items(): 

       html_page = genre + ".html"
       fp = open(html_page, "wb")
       fp.write(urllib.request.urlopen(url).read())
       fp.close()

   print('Enter a genre from the list : ', list(films.keys()))
   genre = input()

   genre_file = genre + ".html"
   fp = open(genre_file)

   #store the html data line by line in a list for parsing
   for data in fp:

       data = data.strip()
       movie_file_list.append(data)

   fp.close()

   for data in movie_file_list:

       pattern = re.findall('<a href="/m/.*" class="unstyled articleLink">', data)
       if pattern:
     
         count += 1
         url = data.split('/')[2].split('"')[0]  
         movie = movie_file_list[index+1].split('<')[0]
         movie_dict.update({movie:url})
         print(str(count)+') '+movie)
       index += 1   

   print('\nEnter a movie from the above list : ')
   movie = input()
   movie = movie.strip()

   url = 'https://www.rottentomatoes.com/m/' + movie_dict[movie]
   movie_page = movie.replace(" ", "") + ".html"

   fp = open(movie_page, "wb")
   fp.write(urllib.request.urlopen(url).read())
   fp.close()
   
   f = open(movie_page, "r")
   movieContent = f.read() 
   lexer = lex()
   parser = yacc()
  
   lexer.input(movieContent) 
   parser.parse(movieContent)
   
   print('\n*******MOVIE INFORMATION*******\n')
   for field, info in result.items():
       print(field, ":", info, '\n')

   print('Director List : ', director, '\n')
   print('Producer List : ', producer, '\n')
   print('Writer List : ', writer, '\n')

   
   print('\n*******CAST INFORMATION*******\n')
   
   length = len(movie_name)
   for index in range(length):
       print(actual_name[index], ":", movie_name[index])
     
   f = open("logfile.txt", "a")
   
   while 1:
       print('\nDo you want to enter a movie field? (y/n)')
       reply = input()
       if reply[0] == 'n' or reply[0] == 'N':
         break
        
       print('\nEnter a field name (without the index number!) from the list below: \n')
       print('1. Movie Name\n2. Director\n3. Writer\n4. Producer\n5. Original Language\n6. Cast\n7. Storyline\n8. Box Office Collection\n9. Runtime\n\nUser Response : ')
     
       Field_requested = input()
       Field_requested = Field_requested.strip()
     
       if Field_requested == 'Movie Name' :
         f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+result['Movie Name']+'>'+'\n')
        
      elif Field_requested == 'Original Language' :
         f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+result['Original Language']+'>'+'\n')
  
      elif Field_requested == 'Storyline' :
         f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+result['Storyline']+'>'+'\n')
        
      elif Field_requested == 'Box Office Collection' :
         f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+result['Box Office Collection']+'>'+'\n')
        
      elif Field_requested == 'Runtime' :
         f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+result['Runtime']+'>')
        
      elif Field_requested == 'Director' :
         length = len(director)
        
         for index in range(length):
           f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+director[index]+'>'+'\n')      
          
      elif Field_requested == 'Producer' :
        length = len(producer)
        
        for index in range(length):
           f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+producer[index]+'>'+'\n')  
          
     elif Field_requested == 'Writer' :
        length = len(writer)
        
        for index in range(length):
           f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+writer[index]+'>'+'\n')              
        
     elif Field_requested == 'Cast' :
        length = len(movie_name)
        
        for index in range(length):
           f.write('<'+ genre +'>'+'<'+movie+'>'+'<'+Field_requested+'>'+'<'+actual_name[index] + ':' + movie_name[index]+'>'+'\n')   
          
     else:
        print('Oops! Field names are case sensitive. Please enter the field names exactly as given in the list.')       
        
   f.close()   
  
   
if __name__ == '__main__':
	main()
