#arr = [4, 6, 1, 3, 5, 7, 25]
#def draw_stars():
#    for i in arr:
#        i = '*' * i
#        print i
#draw_stars()


#Create a function called draw_stars() that takes a list of numbers and prints out *.
#------------------------------------------------------------------

array = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars():
    for i in array:
        if isinstance(i,int):
            i= '*' * i
            print i
           # print '*' * i
        else:
            
            i = i[0] *  len(i)
            x=i.lower()
            print x

           # print i[0].lower()*len(i)
       
draw_stars()