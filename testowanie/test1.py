import matplotlib.pyplot as plt
import pandas as pd
print("test")
print("test1")

x = [1,2,3,4,5,6,7,8,9]
x_dict = pd.DataFrame(x)
print(x_dict)
plt.plot(x_dict)
plt.show()