#code by Sai Teja
#sorting_of_pages() function takes dictionary as input and processes in descending
#order, removes the values with zero strength adn return a maximum of 5 pages in 
#string format.

                                                             
import operator                                                                       #importing operator module

def sorting_of_pages(dict1)->str:                                                     #function accepts dictionary 
  s1=''                                                                               
  sorted_d = dict(sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))     #sorting the dictionary in descending order of query strength
  sorted_d={x:y for x,y in sorted_d.items() if y!=0}                                  #removing the query with zero strength value                                                
  i=1                                                                                 #initializing a counter for 5 maximum pages

  for item in sorted_d.keys():
    if i>5:                                                                           #termination condition if no of pages is greater than 5
      break
    s1=s1+item+' '
    i+=1

  return(s1.strip())                                                                  #returning the string form of list with expected formatting


#Code by Rushikesh
#search() function takes query list as input and matches with each page lists
#if query matches search() function calculates the strength of query and stores
#it in new dictionary and passes the value to sorting_of_pages() for formatting.

def search(lst):
  dict1={}                                            #empty dictionary to store the query page number and its strength

  for key in PAGE_DICT.keys():                        #iterating over keys of Page
    strength=0
    list2=PAGE_DICT[key]                              #making a list of page values

    for i in range(len(lst)):                         #iterating over length of query keywords
      if lst[i] in list2:                             #check for the match of query in page
        strength+=(8-i)*(8-list2.index(lst[i]))       #calculating the strength of query
        
    dict1[key]=strength
  return(sorting_of_pages(dict1))                     #calling the function to sort and format query with strength


#code by Rushikesh
#compute() function iterates over query dictionary and pasess the list of
#query keywords to search() function for computing strength. 

def compute():
  print("Query Pages")
  
  for key in QUERY_DICT.keys():                 #iterating over query dictionary to fetch query keywords
    print(key+": "+search(QUERY_DICT[key]))     #display output: Q1: P1 P3 P5


#code by Rahul Tiwari
#page() function accepts page keyword as String and counter as int and adds
#it to the global PAGE_DICT dictionary

def page(string:str,counter:int):           #function for adding string in page dictionary
  string=string[2:]
  list1=string.split()
  PAGE_DICT['P'+str(counter)]=list1          #adding individual keywords as list

#code by Rahul Tiwari
#query() function accepts query keyword as String and counter as int and adds
#it to the global QUERY_DICT dictionary

def query(string,counter:int):              #function for adding string in query dictionary
  string=string[2:]
  list1=string.split()
  QUERY_DICT['Q'+str(counter)]=list1        #adding individual keywords as list 
  
  #code by Sai Kiran
#declaring global dictionary

PAGE_DICT={}
QUERY_DICT={}

#code by Sai Kiran
#page_selection() is the driving function, this functions takes all the inputs 
#in prescribed and calls page() and query() function and calls compute() function
#to move to the computation and display part of program

def page_selection():                           #driver function
      counter1=1                                #counter for Page 
      counter2=1                                #counter for Query

      while(True):
        n=input().lower()                        #user input as String

        if n=='':
          print("Blank input not accepted")  

        elif n[0] is 'p':
          page(n,counter1)        #calling page function to add in Page dictionary
          counter1+=1

        elif n[0] is 'q':
          query(n,counter2)       #calling query function to add in Query dictionary
          counter2+=1

        elif n[0] is 'e':         #exit control
          break
      compute()                   #calling function for computation
      
page_selection()                  #start point for code
