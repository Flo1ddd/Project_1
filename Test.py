import math

def compute_population(t):
   #вычислить численность населения для года t по формуле
   c = (172/45)*((math.pi/2) - math.atan((2000-t)/45))
   return c

#ввести строку с перечисленными через пробел годами
line = input()

# преобразовать строку в список из строковых значений годов
years_str_list = line.split()

# вычислить количество элементов в списке
n = len(years_str_list)

# сформировать список years_list на основе years_str_list,
#преобразовав строковые значения в целые
years_list = [float(x) for x in years_str_list]

# создать список population_list, каждый элемент которого вычисляется
# функцией compute_population от соответсвующего года из списка years_list
population_list = [compute_population(i) for i in years_list]


# в цикле для каждого года вывести численность населения, для вывода использовать
# формат "%5d - %6.3f миллиард(ов)"
for y in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[y], population_list[y]))
