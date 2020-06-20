import csv #import csv libary to read comma seperated value file
import matplotlib.pyplot as plt  #import matplotlib as plt for effiency
from pylab import ylabel, xlabel  #importing whats needed for graph from pylab

x = []
y = [] #empty list to dispaly x and y graph

with open(r'csv_data\annual_ocean_ph.csv', 'r') as f: #open "anmean file" and read it
    reader = csv.reader(f, delimiter=',') #reader variable to skip all commas in csv
    header = next(reader) #this skips the first line as it contains characters and not integers
    rows = [[row[0], float(row[1])] for row in reader] #defines row as being first row(0) and second row(1) which is converted to a float as it contains decimals 
    for row in (rows): #loop through each row as defined
        x.append(row[0][2:4]) #indexes first row and using dictionaries only takes third and fourth integer since thats all whats needed for years i.e 17, 18, 19.
                               #appends this to empty x list above
        
        y.append(row[1]) #appends first row integers to empty y list as above


plt.plot(x, y, '-2', label="Ocean Ph value") #plots x and y list values appended above
plt.legend(loc="upper right") #shows label in upper right, away from graph
ylabel("Ocean Ph value") #label x axis "Ph value"
xlabel("Time in years") #label y axis with years
plt.show()  #show plot
#plt.savefig("Ph_plot.png") #this line is what saved the plot as an image, not needed as image already stored