import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

state_names = np.array([
	"Alabama",
	"Alaska",
	"Arizona",
	"Arkansas",
	"California",
	"Colorado",
	"Connecticut",
	"Delaware",
	"District of Columbia",
	"Florida",
	"Georgia",
	"Hawaii",
	"Idaho",
	"Illinois",
	"Indiana",
	"Iowa",
	"Kansas",
	"Kentucky",
	"Louisiana",
	"Maine",
	"Maryland",
	"Massachusetts",
	"Michigan",
	"Minnesota",
	"Mississippi",
	"Missouri",
	"Montana",
	"Nebraska",
	"Nevada",
	"New Hampshire",
	"New Jersey",
	"New Mexico",
	"New York",
	"North Carolina",
	"North Dakota",
	"Ohio",
	"Oklahoma",
	"Oregon",
	"Pennsylvania",
	"Rhode Island",
	"South Carolina",
	"South Dakota",
	"Tennessee",
	"Texas",
	"Utah",
	"Vermont",
	"Virginia",
	"Washington",
	"West Virginia",
	"Wisconsin",
	"Wyoming",
	# "U.S. Total"
])

lane_miles = np.array([
	209560,
	35908,
	146761,
	204105,
	396616,
	185827,
	45899,
	14119,
	3448,
	276289,
	273086,
	9804,
	109059,
	306748,
	203045,
	235669,
	286087,
	167145,
	134135,
	46801,
	71244,
	77804,
	256295,
	291814,
	162160,
	278101,
	150133,
	194080,
	100941,
	33448,
	85191,
	150747,
	240827,
	229902,
	179369,
	262465,
	239687,
	161989,
	252038,
	12737,
	166541,
	166098,
	203899,
	686281,
	102452,
	29262,
	164585,
	168271,
	80176,
	239526,
	62575,
	# 8790746
])

population = np.array([
	5039877,
	733391,
	7276316,
	3011524,
	39237836,
	5812069,
	3605944,
	989948,
	689545,
	21781128,
	10799566,
	1455271,
	1839106,
	12671469,
	6805985,
	3190369,
	2937880,
	4505836,
	4657757,
	1362359,
	6165129,
	6984723,
	10050811,
	5707390,
	2961279,
	6168187,
	1084225,
	1961504,
	3104614,
	1377529,
	9267130,
	2117522,
	19835913,
	10551162,
	779094,
	11780017,
	3959353,
	4237256,
	12964056,
	1097379,
	5190705,
	886667,
	6975218,
	29527941,
	3271616,
	643077,
	8642274,
	7738692,
	1793716,
	5895908,
	576851,
	# 331700114
])

land_area = np.array([
	50645.33,
	570640.95,
	113594.08,
	52035.48,
	155779.22,
	103641.89,
	4842.36,
	1948.54,
	61.05,
	53624.76,
	57513.49,
	6422.63,
	82643.12,
	55518.93,
	35826.11,
	55857.13,
	81758.72,
	39486.34,
	43203.90,
	30842.92,
	9707.24,
	7800.06,
	56538.90,
	79626.74,
	46923.27,
	68741.52,
	145545.80,
	76824.17,
	109781.18,
	8952.65,
	7354.22,
	121298.15,
	47126.40,
	48617.91,
	69000.80,
	40860.69,
	68594.92,
	95988.01,
	44742.70,
	1033.81,
	30060.70,
	75811.00,
	41234.90,
	261231.71,
	82169.62,
	9216.66,
	39490.09,
	66455.52,
	24038.21,
	54157.80,
	97093.14,
	# 3531905.44
])

# auxilliary data
population_density = population / land_area
lane_miles_per_person = lane_miles / population
road_network_density = lane_miles / land_area
size = population / 100000
colors = np.random.rand(len(state_names))

# annotate the given state
def annotate(state, x_list, y_list):
	x_offset = max(x_list) / 50
	y_offset = max(y_list) / -100
	i = np.where(state_names == state)
	x = x_list[i] + x_offset
	y = y_list[i] + y_offset
	# plt.text(x, y, state)
	plt.annotate(state, (x, y))

def plot():
	plt.scatter(population_density, road_network_density, s=size, c=colors, alpha=.5)

	# log-log regression
	log_regression = stats.linregress(np.log2(population_density), np.log2(road_network_density))
	x_min = min(population_density)
	x_max = max(population_density)
	regression_x = np.arange(x_min, x_max, (x_max - x_min) / 100)
	regression_y = 2 ** (log_regression.intercept + log_regression.slope * np.log2(regression_x))
	plt.plot(regression_x, regression_y, 'r', alpha=.5, label='log-log regression, r^2 = {:0.2f}'.format(log_regression.rvalue ** 2))

	plt.xlabel("population density (people per square mile)")
	plt.ylabel("road network density (lane miles per square mile)")
	plt.legend()

### on linear scale ###
plot()
for state in ["New Jersey", "Rhode Island", "Connecticut", "Alaska", "California", "Hawaii", "Maryland", "Massachusetts", "Ohio", "New York", "Texas", "Virginia", "District of Columbia"]:
	annotate(state, population_density, road_network_density)
plt.show()

### on log scale ###
plot()
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.show()