import csv #import csv libary to read comma seperated value file
import matplotlib.pyplot as plt #import matplotlib as plt for effiency
from pylab import ylabel, xlabel #importing whats needed for graph from pylab

x = []
y = [] #empty list to dispaly x and y graph

with open(r'csv_data\annaul_Co2_emission.csv', 'r') as f: #open "anmean file" and read it
    reader = csv.reader(f, delimiter=',') #reader variable to skip all commas in csv
    header = next(reader) #this skips the first line as it contains characters and not integers
    rows = [[row[0], float(row[1])] for row in reader] #defines row as being first row(0) and second row(1) which is convetred to a float as it contains decimals 
    for row in (rows): #loop through each row as defined
        x.append(row[0][2:4]) #indexes first row and using dictionaries only takes third and fourth integer since thats all whats needed for years i.e 17, 18, 19.
                              #appends this to empty x list above
        
        y.append(row[1]) #appends first row integers to empty y list as above


plt.plot(x, y, 'k-1', label="Co2 in PPM") #plots x and y list values appended above, 'k' makes the line black
ylabel("Co2 in PPM") #label y axis "Co2 in PPM"
plt.legend(loc="upper left") #shows label in upper left, away from graph
xlabel("Time in years")#label x axis "Time in years"
plt.show() #show plot
#plt.savefig("Co2_plot.png") #this line is what saved the plot as an image, not needed as image already stored