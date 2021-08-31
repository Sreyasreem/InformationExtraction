import urllib.request, urllib.error, urllib.parse
import re
from ply.lex import lex
from ply.yacc import  yacc


# tokens list
tokens = (
	'LMOVIE', 'BOXOFFICE', 'LLANGUAGE',
        'LSTORY', 'RUNTIME', 'LDIR', 'CELEBRITY', 
        'onlineplatform', 'separator', 'ACTUALNAME',
        'CHARNAME', 'similarMov', 'LINK', 'HIGHF', 'LOWF', 
        'BDATE', 'MOVIELIST', 'MYEAR', 'similarMovLink'
    )

#basic movie info
result = {}

#director list
director = []

#writer list
writer = []

#producer list
producer = []

#Cast list
actual_name = {}

#Movie character list
movie_name = {}

#you might also like 
sim_movie = {}

#available platforms
platform = []

#basic info of actor
result_profile = {}

#movie list of actor
m_list = {}


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
    
def t_LLANGUAGE(t):
    r'<div\s+class="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Original\sLanguage:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">(.+)'

    t.value = t.lexer.lexmatch.groups()[5].strip()
    
    return t

#Run Time
def t_RUNTIME(t):
    r'<div\s+class="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Runtime:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">[\s\S]*?<time\sdatetime=".*">[\s\S]*?(.+)'
    t.value = t.lexer.lexmatch.groups()[7].strip()

   
    return t

#storyline
def t_LSTORY(t):
    r'<div\sid="movieSynopsis"\sclass="movie_synopsis\sclamp\sclamp-6\sjs-clamp"\sstyle="clear:both"\sdata-qa="movie-info-synopsis">[\s\S]*?(.+)'
    t.value = t.lexer.lexmatch.groups()[9].strip()
    
    return t

#director                   
def t_LDIR(t):
    r'<a\s+href="/celebrity/.+"\sdata-qa="movie-info-director">(.+)</a>'
    t.value = t.lexer.lexmatch.groups()[11].strip()

    return t

#celebrity
def t_CELEBRITY(t):
    r'<a\s+href="/celebrity/.+">(.+)</a>'  
    t.value = t.lexer.lexmatch.groups()[13].strip()

    
    return t

#separator token
def t_separator(t):
    r'<div\sclass="meta-label\ssubtle"\sdata-qa="movie-info-item-label">Writer:</div>[\s\S]*?<div\sclass="meta-value"\sdata-qa="movie-info-item-value">[^<]*?'
    
    return t


#real name of the actor
def t_ACTUALNAME(t):

    #r'<a\shref="\s.*/celebrity/.*\s"\sclass="unstyled\sarticleLink"\sdata-qa="cast-crew-item-link">\n.*\n.*<span\stitle="(.*)">'
    r'<a\shref="\s.*/celebrity/.*\s"\sclass="unstyled\sarticleLink"\sdata-qa="cast-crew-item-link">[\s\S]*?<span\stitle="(.*)">'

    t.value = t.lexer.lexmatch.groups()[16].strip()

    return t

#movie name of the actor    
def t_CHARNAME (t):

    r'<span\sclass="characters\ssubtle\ssmaller"\stitle=".*">[\s\S]*?<br/?>\n.*\n([a-z|A-Z|0-9|\'\"\^\*\(\)\.\+\-\\,:\n\s!@#$%&*]+)<br/?>'
    
    name_list = []
    group_tk = t.lexer.lexmatch.groups()[18].strip().split("\n")
    
    for val in group_tk:
        name_list.append(val.strip())
        
    t.value = (' '.join(name_list))

    return t

#you might also like
def t_similarMov(t):

    r'<span\sslot="title"\sclass="recommendations-panel__poster-title">(.+)</span>'
    t.value = t.lexer.lexmatch.groups()[20].strip()

     
    return t

#available platforms
def t_onlineplatform(t):
    r'<a\sclass="affiliate__link\saffiliate__link--veneer\sjs-affiliate-link"\sdata-affiliate="(.+)"\starget'

    t.value = t.lexer.lexmatch.groups()[22].strip()
     
    return t

#actor/actress profile url
def t_LINK(t):
    r'<a\shref="(.*)"\sdata-qa="cast-crew-item-img-link">'
    t.value = t.lexer.lexmatch.groups()[24].strip()
    
    return t   


#Highest rated film
def t_HIGHF(t):
    r'Highest\sRated:[\s\S]*?<a\sclass="celebrity-bio__link"\shref="/m/.*">\n(.*)\n.*</a>'
    t.value = t.lexer.lexmatch.groups()[26].strip()
    
    return t    


#Lowest rated movie
def t_LOWF(t):

    r'Lowest\sRated:[\s\S]*?<a\sclass="celebrity-bio__link"\shref="/m/.*">\n(.*)\n.*</a>'
    t.value = t.lexer.lexmatch.groups()[28].strip()


    return t


#birthdate of the actor
def t_BDATE(t):
    r'<p\sclass="celebrity-bio__item"\sdata-qa="celebrity-bio-bday">\n.*Birthday:\n(.*)'
    t.value = t.lexer.lexmatch.groups()[30].strip()

    
    return t


#movie list of the actor/actress    
def t_MOVIELIST(t):

    r'data-qa="celebrity-filmography-movies-trow">[\s\S]*?<td\sclass="celebrity-filmography__title">[\s\S]*?<(.+)'
    t.value = t.lexer.lexmatch.groups()[32].split('>')[1].split('<')[0]
    #r'<td\s+class="celebrity-filmography__title">[\s\S]*?<a\s+href="/m/.*">(.+)<'
    #t.value = t.lexer.lexmatch.groups()[32].strip()
    
    return t


#Year of film release
def t_MYEAR(t):

    r'<td\sclass="celebrity-filmography__box-office"\sdata-qa="celebrity-filmography-movies-trow-boxofficeData">[\s\S]*?<td\sclass="celebrity-filmography__year">(.+)</td>'
    t.value = t.lexer.lexmatch.groups()[34].strip()
    
    return t

#movie links of similar movies
def t_similarMovLink(t):
    r'<a\shref="(.*)"\sclass="recommendations-panel__poster-link">'
    t.value = t.lexer.lexmatch.groups()[36].strip()
    
    return t
    
                
# Error handling rule
def t_error(t):
    t.lexer.skip(1)


# Parsing Rules
def p_start(p):
	'''start :  moviename simMov whereTowatch storyline language director producer writer boxoffice runtime crew 
	         |  highestRated lowestRated birthday exception movieList
	         |  highestRated lowestRated birthday movieList
			 '''
	pass    

#Movie name
def p_moviename(p):
    '''moviename : LMOVIE
                 | epsilon '''
    
    if p[1]:
       result['Movie Name'] = p[1]
       
    else:
       result['Movie Name'] = 'N/A'

    pass

#you might also like section
def p_simMov(p):

    '''simMov : simMov dmov
              | dmov'''

    pass
     
def p_dmov(p):
    '''dmov : similarMovLink similarMov
            | similarMovLink epsilon
            | epsilon similarMov '''

    
    if p[1] and p[2]:
       sim_movie[p[2]] = 'https://www.rottentomatoes.com'+p[1] 
       
    elif p[2] and (p[1] == None):
         sim_movie[p[2]] = 'N/A' 
                 
    pass

#online platforms
def p_whereTowatch(p):

    '''whereTowatch : whereTowatch dwatch
                    | dwatch'''

    pass
     
def p_dwatch(p):
    '''dwatch : onlineplatform
              | epsilon '''

    if p[1]:
       platform.append(p[1])
          
    pass


#Movie storyline           
def p_storyline(p):
    '''storyline : LSTORY 
                 | epsilon '''

    if p[1]:
       result['Storyline'] = p[1]
       
    else:
       result['Storyline'] = 'N/A'

    pass

#Movie original language
def p_language(p):
    '''language : LLANGUAGE 
                | epsilon '''
    
    if p[1]:
       result['Original Language'] = p[1]
       
    else:
       result['Original Language'] = 'N/A'

    pass

#Movie director(s)              
def p_director(p):
    '''director : director dval 
                | dval'''

    pass


def p_dval(p):
    '''dval : LDIR
            | epsilon '''
    
    if p[1]:
       director.append(p[1])

    pass    

#Movie producer(s)   
def p_producer(p):
    '''producer : lprod producer
                | lprod'''  
               
    pass           

#Movie writer(s)
def p_writer(p):
    '''writer : separator lwrite writer
              | lwrite writer
              | lwrite'''

    pass

def p_lwrite(p):
    '''lwrite : CELEBRITY
              | epsilon '''
    
    if p[1]:
       writer.append(p[1])

    pass 
 
def p_lprod(p):
    '''lprod : CELEBRITY
             | epsilon '''
    if p[1]:
       producer.append(p[1])
    
    pass 

#Movie boxoffice                     
def p_boxoffice(p):
    '''boxoffice : BOXOFFICE 
                 | epsilon '''
                 

    if p[1]:
       result['Box Office Collection'] = p[1]
       
    else:
       result['Box Office Collection'] = 'N/A'   

    pass

#Movie runtime    
def p_runtime(p):
    '''runtime : RUNTIME 
               | epsilon '''

    if p[1]:
       result['Runtime'] = p[1] 
    
    else: 
       result['Runtime'] = 'N/A'  

    pass

#Movie cast
def p_crew(p):
    '''crew : crew lcast
            | lcast ''' 


    pass
    
def p_lcast(p):
    '''lcast : LINK ACTUALNAME CHARNAME
             | LINK ACTUALNAME epsilon 
             | LINK epsilon CHARNAME 
             | epsilon ACTUALNAME CHARNAME 
             | epsilon ACTUALNAME epsilon ''' 
    
    
    if p[2] and p[3]:
    
       movie_name[p[2]] = p[3]
       
       if p[1]:
          actual_name[p[2]] = 'https://www.rottentomatoes.com'+p[1]
          
       else:
          actual_name[p[2]] = 'N/A'
             
       
    pass  

#Actor highest rated film                                    
def p_highestRated(p):
    '''highestRated : HIGHF
                    | epsilon '''
    
    if p[1]:
       result_profile['HighestRated'] = p[1]
       
    else: 
       result_profile['HighestRated'] = 'N/A'   
       
    pass

#Actor lowest rated film                                    
def p_lowestRated(p):
    '''lowestRated : LOWF
                   | epsilon '''
                 
    if p[1]:
       result_profile['LowestRated'] = p[1]
    
    else: 
       result_profile['LowestRated'] = 'N/A'   
       
    pass    

#Actor birthday                                         
def p_birthday(p):
    '''birthday : BDATE
                | epsilon '''
    if p[1]:            
       result_profile['Birthday'] = p[1]
     
    else: 
       result_profile['Birthday'] = 'N/A'   

    pass 

def p_exception(p):
    'exception : CELEBRITY'
     
    pass 
     
#Actor movie list
def p_movieList(p):
    '''movieList : mlist movieList
                 | mlist'''
    pass
     
def p_mlist(p):

    '''mlist : MOVIELIST MYEAR
             | MOVIELIST epsilon
             | epsilon MYEAR '''
    
    if p[1] and p[2]:
       m_list[p[1]] = p[2]
       
       
    elif p[1] and (p[2] == None):
         m_list[p[1]] = 'N/A'
            
    
    pass


def p_epsilon(p):
    'epsilon : '
    
    pass
    
def p_error(t):
    pass
        

def main():
    
   #download and save the genre html files
   for genre, url in films.items(): 
   
       html_page = genre + ".html"
       fp = open(html_page, "wb")
       fp.write(urllib.request.urlopen(url).read())
       fp.close()
   
   #perform webpage extraction
   root_function()
   
#extract movie names from the genre files
def root_function():

    while 1: 
  
       #file index
       index = 0
   
       #movie index
       count = 0
       
       #dictionary of the urls of the 100 movies
       movie_dict = {}
       
       #html file of movie
       movie_file_list = []
       
       print('HELLO! WE ARE AT THE ROOT NOW.')
       print('\nDo you want a new movie information? (y/n)')
       reply = input()
       
       if reply[0] == 'n' or reply[0] == 'N':
          break
          
       print('Enter a genre from the list : ', list(films.keys()))

       genre = input()
       genre = genre.strip()

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
   
       MovieParsing(movie, url)
       
#Generate tokens and parse the movie page     
def MovieParsing(movie, url):
   
   #re-initialize the data structures for every movie
   result.clear() 
   director.clear()  
   writer.clear()  
   producer.clear()  
   actual_name.clear()  
   movie_name.clear()  
   sim_movie.clear()  
   platform.clear()  
   
   movie_page = movie.replace(" ", "") + ".html"
   
   fp = open(movie_page, "wb")
   fp.write(urllib.request.urlopen(url).read())
   fp.close()
   
   f = open(movie_page, "r") 
   
   movieContent = f.read() 
   f.close()
   
   lexer = lex()
   parser = yacc()
   lexer.input(movieContent)
   '''
   #tokens for movie page
   while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)
   '''
   parser.parse(movieContent)
   
   MovieInfo()
   
#Display movie information 
def MovieInfo():
    
   #local data structures
   result_local      = result.copy()
   director_local    = director.copy()
   producer_local    = producer.copy()
   writer_local      = writer.copy()
   actual_name_local = actual_name.copy()
   movie_name_local  = movie_name.copy()
   sim_movie_local   = sim_movie.copy()
   platform_local    = platform.copy()
   
   '''
   print('basic info:',result_local)
   print('director:',director_local)
   print('producer:',producer_local)
   print('writer:',writer_local)
   
   for realn, charn in movie_name_local.items():
       print(realn, ":", charn)
    
   for state in sim_movie_local:
       print(state)
       
   print('platforms:',platform_local)
   '''
   while 1:
       print('\nDo you want to enter a field from the movie,',result_local['Movie Name'],'? (y/n)')
       reply = input()
       if reply[0] == 'n' or reply[0] == 'N':
          break  
         
       print('\nEnter a field name (WITHOUT the index number!) from the list below: \n')
       print('1. Movie Name\n2. Director\n3. Writer\n4. Producer\n5. Original Language\n6. Cast\n7. Storyline\n8. Box Office Collection\n9. Runtime\n10. YOU MIGHT ALSO LIKE\n11. WHERE TO WATCH\n\nUser Response : ')  
       
       Field_requested = input()
       Field_requested = Field_requested.strip()
       
       if Field_requested == 'Movie Name' :
          print('Query Result : ',result_local['Movie Name'],'\n')
        
       elif Field_requested == 'Original Language' :
          print('Query Result : ',result_local['Original Language'],'\n')
       
       elif Field_requested == 'Storyline' :
          print('Query Result : ',result_local['Storyline'],'\n')
        
       elif Field_requested == 'Box Office Collection' :
          print('Query Result : ',result_local['Box Office Collection'],'\n')
        
       elif Field_requested == 'Runtime' :
          print('Query Result : ',result_local['Runtime'],'\n')
          
       elif Field_requested == 'Director' :
          length = len(director_local)
        
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             print('Query Result : ', director_local, '\n')  
             
          
       elif Field_requested == 'Producer' :
          length = len(producer_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             print('Query Result : ', producer_local, '\n') 
          
          
       elif Field_requested == 'Writer' :
          length = len(writer_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             print('Query Result : ', writer_local, '\n')
             
       elif Field_requested == 'Cast' :
          length = len(movie_name_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
           
          else:   
             for realN, charN in movie_name_local.items():
                 print(realN, ":", charN) 
                 
             print('\n\nDo you want to go to a profile of an actor/actress from the Cast of the movie,',result_local['Movie Name'],'?(y/n) : ')
             u_reply = input()
             if u_reply[0] == 'n' or u_reply[0] == 'N':
                continue
                
             print('\n\nEnter a name from the above listed CAST : ')
             actor = input()
             actor = actor.strip() 
             
             if actual_name_local[actor] == 'N/A':
                print(actor,'profile not available!\n')
                
             else:   
                castParsing(actor, actual_name_local[actor])
             
                 
       elif Field_requested == 'YOU MIGHT ALSO LIKE' :
          length = len(sim_movie_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             for simList in sim_movie_local:
                 print(simList)
                 
             print('\n\nDo you want a movie information from the list of YOU MIGHT ALSO LIKE of the movie,',result_local['Movie Name'],'?(y/n) : ')
             u_reply = input()
             if u_reply[0] == 'n' or u_reply[0] == 'N':
                continue
             
             print('\n\nEnter a movie name from the list of similar movies : ')
             res = input()
             res = res.strip() 
             
             if sim_movie_local[res] == 'N/A':
                print(res,'webpage not available!\n')
                
             else: 
                MovieParsing(res, sim_movie_local[res])    
                 
       
       elif Field_requested == 'WHERE TO WATCH' :
          length = len(platform_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             print('Query Result : ', platform_local, '\n')
             
       
       else:
          print('Oops! Field names are case sensitive. Please enter the field names exactly as given in the list.')       


#Generate tokens and parse the profile page of actor   
def castParsing(actor, actor_url):  
    
    #re-initialize the data structures for every actor/actress profile
    result_profile.clear()
    m_list.clear()
    
    actor_page = actor.replace(" ", "") + ".html"
    
    #save the actor profile page
    fp = open(actor_page, "wb")
    fp.write(urllib.request.urlopen(actor_url).read())
    fp.close()
    
    fp = open(actor_page, "r") 
    Content = fp.read()
    
    lexer = lex()
    parser = yacc()
    lexer.input(Content)
    '''
    #tokens for actor page
    while True:
        tok = lexer.token()
        if not tok: 
           break      # No more input
        print(tok)
    '''
    parser.parse(Content) 
    
    castInfo(actor)

#Display actor information
def castInfo(actor):
    
    #local data structures
    m_list_local         = m_list.copy()
    result_profile_local = result_profile.copy()
    '''
    print('basic actor info:',result_profile_local)
    for state in m_list_local:
        print(state)
    '''
    while 1:
       print('\nDo you want information regarding ',actor,'? (y/n)')
       reply = input()
       if reply[0] == 'n' or reply[0] == 'N':
          break  
         
       print('\nEnter a field name (WITHOUT the index number!) from the list below: \n')
       print('1. Highest Rated film\n2. Lowest Rated film\n3. Birthday\n4. Movies\n\nUser Response : ') 
       
       Field_requested = input()
       Field_requested = Field_requested.strip()
       
       if Field_requested == 'Highest Rated film' :
          print('Query Result : ',result_profile_local['HighestRated'],'\n')
        
       elif Field_requested == 'Lowest Rated film' :
          print('Query Result : ',result_profile_local['LowestRated'],'\n')
       
       elif Field_requested == 'Birthday' :
          print('Query Result : ',result_profile_local['Birthday'],'\n')
        
       elif Field_requested == 'Movies' :
       
          length = len(m_list_local)
          
          if length == 0:
             print('Query Result : N/A','\n')
            
          else: 
             for movie in m_list_local:
                 print(movie)
                 
             print('\nEnter a year (INTEGER VALUE) to filter out the movies: ')
             reply = input()  
             reply = reply.strip() 
             
             movie_count = 0
             for key, value in m_list_local.items():
             
                 if value == 'N/A':
                    continue
                    
                 if int(value) >= int(reply):
                    movie_count += 1
                    print(value, ":", key)
                    
             if movie_count == 0: 
                print('Query Result : N/A','\n')      
        
       else :
          print('Oops! Field names are case sensitive. Please enter the field names exactly as given in the list.') 
    
             
if __name__ == '__main__':
	main()        
           
