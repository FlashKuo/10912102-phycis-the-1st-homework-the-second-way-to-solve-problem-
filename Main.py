from myMath import myArithmetic,myCalcArea,myStatistics
the_first_number=float(input('input your first number:'))
the_second_number=float(input('input your second number:'))
the_third_number=float(input('input your third number:'))
the_fourth_number=float(input('input your fourth number:'))
the_fifth_number=float(input('input your fifth number:'))
list_of_number=[the_first_number,the_second_number,the_third_number,the_fourth_number,the_fifth_number]
print(myStatistics.myMean(list_of_number))
