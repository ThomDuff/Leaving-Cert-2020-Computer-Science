import csv #import csv libary to read comma seperated value file
import matplotlib.pyplot as plt #import matplotlib as plt for effiency
from pylab import figure, show, legend, ylabel, xlabel #importing whats needed for graph from pylab
fig = figure() #creates figure object which allows us to change how graph looks, allowing us two plot 2 grpahs at once

x1 = []
y1 = [] #first empty list for one graph 

x2 = []
y2 = []#second empty list for other graph

def clean(x, y): #function to clean, parsing x and y lists
    reader = csv.reader(f, delimiter=',') #reader variable to skip all commas in csv
    header = next(reader) #this skips the first line as it contains characters and not integers
    rows = [[row[0], float(row[1])] for row in reader] #defines row as being first row(0) and second row(1) which is convetred to a float as it contains decimals 
    for row in (rows): #loop through each row as defined
        x.append(row[0][2:4]) #indexes first row and using dictionaries only takes third and fourth integer since thats all whats needed for years i.e 17, 18, 19.
                              #appends this to empty x list above
        
        y.append(row[1]) #appends first row integers to empty y list as above

with open(r'csv_data\annaul_Co2_emission.csv', 'r') as f: #opens Co2 data file and reads it
    clean(x1, y1) #calls funtion parsing x1 and y1 to be appended with data
  
    
with open(r'csv_data\annual_ocean_ph.csv', 'r') as f: #opens Ph data file and reads it
    clean(x2, y2) #calls funtion parsing x2 and y2 to be appended with data 

#This plots the Ph graph
ax = fig.add_subplot(111) #variable "ax" is figure object with subplot which is used to plot 2 graphs, "111" is the paramneters to make 1*1 grid
line1 = ax.plot(x2, y2, '-2') #variable to plot first line. Plots appended Ph lists from above
ylabel("Ph level") #label y axis "Ph level" on left



#This plots the Co2 graph
ax = fig.add_subplot(111, sharex=ax, frameon=False)  #same as line 30. "sharex" allows to share axis between plots. "frameon" is frame on plot set to flase to not apppear
line2 = ax.plot(x1, y1, 'k-1') #variable to plot second line. Plots appended Co2 lists from above, "k" makes line black to look different and stop confusion
ax.yaxis.tick_right() #puts y axis on right, this being the Co2 in ppm 
ax.yaxis.set_label_position("right") #puts Co2 y axis label on right, helps user
ylabel("Co2 in Parts Per Million") #label this y axis "Ph level" on left
xlabel("Times in years") #labels x axis "Time in years", this x axis is shared between the two y axis

plt.show() #shows plot when ran
#plt.savefig("Both_Plot.png") #this line is what saved the plot as an image, not needed as image already stored

