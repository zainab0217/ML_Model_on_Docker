import pandas
from sklearn.linear_model import LinearRegression
import numpy
marks = [60,20,70,80,10]
hours = [6,2,7,8,1]

marks = numpy.array(marks)
hours = numpy.array(hours)
hours = hours.reshape(-1,1)
jack_hours = [[4]]
mind = LinearRegression()
mind.fit(hours,marks)
jack_marks = mind.predict(jack_hours)
mind.predict([[5]])

