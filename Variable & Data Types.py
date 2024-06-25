#Data Types - Data types are used to define  what type of data we are going to sotre in a variable.
# Types of Data type in Python
'''
1. Numeric type 
 - Integers 
 - Floats 
 - Complex 
 - Boolean

2. Sequence Type
- List
- Tuple
- String

2. Dictionary 

4. Set

'''

#1. Numeric type - Python numeric data types store numeric values.
#Examples of Numeric Data Types
# Integer Numeric Data types
intNum =25
print(intNum," is ",type(intNum))
# Output :- 25  is  <class 'int'>

# Float Numeric Data types
floatNum =17.254
print(floatNum , " is ",type(floatNum))
# Output :- 17.254  is  <class 'float'>

# Complex Numeric Data types
complexNum =21+5j
print(complexNum, " is ", type(complexNum))
# Output :-(21+5j)  is  <class 'complex'>

# Boolean Numeric Data types
BooleanIsmale = True
print(BooleanIsmale, " is ", type(BooleanIsmale))
# Output :- True is <class 'bool'>

#Sequence Type 
#List Data Type - Python list are similar to arrays.
#example
listData= [2024,"June",21.5,55+6j]
print(listData,type(listData))
#Output :- [2024, 'June', 21.5, (55+6j)] <class 'list'>

# Tuple Data type - is another sequence data type that is similat to a list.
#Example
tupleData = ('abc',123,3.33)
print(tupleData,type(tupleData))
#Output :- ('abc', 123, 3.33) <class 'tuple'>

#String Data type- is a sequence of one or more unicode characters,enclosed in single ,double or triple quotation marks
#Example
stringData="Amit Sakhare"
print(stringData,type(stringData))
#Output :- Amit Sakhare <class 'str'>

# Python Dictionary Data Type - are kind of hash table type, A dictonarty key can be almost any python type.
# Example

dictDaysData ={
    'sun' : 'Sunday',
    'mon' : 'Monday',
    'tue' : 'Tusday',
    'wed' : 'Wendesday',
    'th' : 'Thursday',

}
print(dictDaysData,type(dictDaysData))
#Output :- {'sun': 'Sunday', 'mon': 'Monday', 'tue': 'Tusday', 'wed': 'Wendesday', 'th': 'Thursday'} <class 'dict'>

# Set Data Types - python implementation of set as defined in Mathamatics. A set in python is a collection, but is not an indexed or ordered collection as string.list or tuple.
#Example
setMonthData = {'Jan','Feb','March','April'}
print(setMonthData,type(setMonthData))
#Output :- {'Feb', 'April', 'March', 'Jan'} <class 'set'>



#Variables - Python Variables are container to store values to memory locations . that means when you create variable you resrve some space in memory.
#Example 
name = "Amit Sakhare" # name is variable and Amit sakhare is store value in name variable.
print(name)
#Output :- Amit Sakhare