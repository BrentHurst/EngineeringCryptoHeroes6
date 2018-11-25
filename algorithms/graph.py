import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('naive algorithm', 'moving average', 'machine learning')
y_pos = np.arange(len(objects))
performance = [988.01,984.25,987.50]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Total Asset')
plt.title('Simulated 1 month daily trading')
plt.ylim((900,1000))
plt.savefig('img/simulated_1month.png')  
plt.show() 
