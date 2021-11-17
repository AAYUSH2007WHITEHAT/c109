import pandas as pd
import csv
import statistics

df = pd.read_csv("data.csv")

height_list = df["Height"].to_list()
weight_list = df["Weight"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("Mean, Median and Mode of height is {}, {} , {} ".format(height_mean, height_median, height_mode))
print("Mean, Median and Mode of weight is {}, {} , {} ".format(weight_mean, weight_median, weight_mode))

height_std_dev = statistics.stdev(height_list)
weight_std_dev = statistics.stdev(weight_list)

height_first_std_dev_start, height_first_std_dev_end = height_mean-height_std_dev, height_mean+height_std_dev
height_second_std_dev_start, height_second_std_dev_end = height_mean-(2*height_std_dev), height_mean+(2*height_std_dev)
height_third_std_dev_start, height_third_std_dev_end = height_mean-(3*height_std_dev), height_mean+(3*height_std_dev)

weight_first_std_dev_start, weight_first_std_dev_end = weight_mean - weight_std_dev, weight_mean + weight_std_dev
weight_second_std_dev_start, weight_second_std_dev_end = weight_mean - (2*weight_std_dev), weight_mean + (2*weight_std_dev)
weight_third_std_dev_start, weight_third_std_dev_end = weight_mean - (3*weight_std_dev), weight_mean+(3*weight_std_dev)

height_list_of_data_within_1_std_dev = [result for result in height_list if result > height_first_std_dev_start and result < height_first_std_dev_end]
height_list_of_data_within_2_std_dev = [result for result in height_list if result > height_second_std_dev_start and result < height_second_std_dev_end]
height_list_of_data_within_3_std_dev = [result for result in height_list if result > height_third_std_dev_start and result < height_third_std_dev_end]

weight_list_of_data_within_1_std_dev = [result for result in weight_list if result > weight_first_std_dev_start and result < weight_first_std_dev_end]
weight_list_of_data_within_2_std_dev = [result for result in weight_list if result > weight_second_std_dev_start and result < weight_second_std_dev_end]
weight_list_of_data_within_3_std_dev = [result for result in weight_list if result > weight_third_std_dev_start and result < weight_third_std_dev_end]

print("{}% Of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_dev)*100/len(height_list)))
print("{}% Of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_dev)*100/len(height_list)))
print("{}% Of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_dev)*100/len(height_list)))

print("{}% Of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_dev)*100/len(weight_list)))
print("{}% Of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_dev)*100/len(weight_list)))
print("{}% Of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_dev)*100/len(weight_list)))
