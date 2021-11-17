import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

count = []
dice_result = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)
    count.append(i)


mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode (dice_result)
standard_deviation = statistics.stdev(dice_result)

print("mean of the data is{}".format(mean))
print("median of the data is{}".format(median))
print("mode of the data is{}".format(mode))
print("standard deviation of the data is{}".format(standard_deviation))	

first_stdev_start,first_stdev_end = mean - standard_deviation,mean + standard_deviation
second_stdev_start,second_stdev_end = mean - (2*standard_deviation),mean + (2*standard_deviation)
third_stdev_start,third_stdev_end = mean - (3*standard_deviation),mean + (3*standard_deviation)
list_in_stdev_1 =[result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
list_in_stdev_2 =[result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
list_in_stdev_3 =[result for result in dice_result if result > third_stdev_start and result < third_stdev_end]
print("{}% Of data lies within 1 standard deviation".format(len(list_in_stdev_1)*100/len(dice_result)))
print("{}% Of data lies within 1 standard deviation".format(len(list_in_stdev_2)*100/len(dice_result)))
print("{}% Of data lies within 1 standard deviation".format(len(list_in_stdev_3)*100/len(dice_result)))