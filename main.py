from sort import *
import time

lista1 = [34, 55, 68, 12, 83, 0, 52, 6, 70, 42, 92, 43, 46, 72, 80, 90, 28, 1, 71, 14, 38, 19, 31, 87, 97, 49, 91, 74, 88, 4, 62, 93, 17, 57, 60, 85, 47, 36, 50, 59, 61, 32, 67, 40, 64, 29, 23, 48, 9, 13, 35, 15, 73, 96, 99, 56, 84, 69, 27, 79, 5, 81, 53, 78, 54, 76, 2, 89, 66, 3, 77, 41, 94, 51, 37, 86, 16, 98, 26, 63, 65, 22, 44, 11, 25, 45, 30, 75, 18, 95, 58, 7, 33, 82, 39, 20, 24, 10, 8, 21]
lista2 = [34, 55, 68, 12, 83, 0, 52, 6, 70, 42, 92, 43, 46, 72, 80, 90, 28, 1, 71, 14, 38, 19, 31, 87, 97, 49, 91, 74, 88, 4, 62, 93, 17, 57, 60, 85, 47, 36, 50, 59, 61, 32, 67, 40, 64, 29, 23, 48, 9, 13, 35, 15, 73, 96, 99, 56, 84, 69, 27, 79, 5, 81, 53, 78, 54, 76, 2, 89, 66, 3, 77, 41, 94, 51, 37, 86, 16, 98, 26, 63, 65, 22, 44, 11, 25, 45, 30, 75, 18, 95, 58, 7, 33, 82, 39, 20, 24, 10, 8, 21]
lista3 = [34, 55, 68, 12, 83, 0, 52, 6, 70, 42, 92, 43, 46, 72, 80, 90, 28, 1, 71, 14, 38, 19, 31, 87, 97, 49, 91, 74, 88, 4, 62, 93, 17, 57, 60, 85, 47, 36, 50, 59, 61, 32, 67, 40, 64, 29, 23, 48, 9, 13, 35, 15, 73, 96, 99, 56, 84, 69, 27, 79, 5, 81, 53, 78, 54, 76, 2, 89, 66, 3, 77, 41, 94, 51, 37, 86, 16, 98, 26, 63, 65, 22, 44, 11, 25, 45, 30, 75, 18, 95, 58, 7, 33, 82, 39, 20, 24, 10, 8, 21]

t0 = time.clock()
print(insertion_sort(lista1))
print('insertion sort time: '+ str(time.clock()-t0))
t0 = time.clock()
print(selection_sort(lista2))
print('selection sort time: '+ str(time.clock()-t0))
t0 = time.clock()
print(bubble_sort(lista3))
print('bubble sort time: '+ str(time.clock()-t0))