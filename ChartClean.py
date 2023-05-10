import matplotlib.pyplot as plt

# Open the file and read the data
with open('outputfile.txt', 'r') as f:
    lines = f.readlines()

# Parse the data into two lists: names and integers
names = []
integers = []
for line in lines:
    parts = line.strip().split(': ')
    names.append(parts[0].replace('$', '\$'))
    integers.append(int(parts[1]))

# Sort the names and integers lists in descending order by ms played
sorted_data = sorted(zip(integers, names), reverse=True)[:15]
integers, names = zip(*sorted_data)

# Create the bar graph
plt.bar(names, integers)
plt.xticks(rotation=90)
plt.xlabel('Names')
plt.ylabel('MS played')
plt.title('Top 10 artists by milliseconds played')
plt.show()