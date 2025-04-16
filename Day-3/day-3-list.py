# -------------------------------------------------------------------------
# List, Tuple, Set
# Collection of items:
# string_1, string_2, string_3
# num_1, num_2, num_3
# string_1, num_5, boolean_1

# Feature	    List ([])                     Tuple (())	               Set ({} or set())
# Mutable	    ✅ Yes	                    ❌ No	                    ✅ Yes
# Ordered	    ✅ Yes (preserves order)	    ✅ Yes (preserves order)	    ✅ Yes (Python 3.7+)
# Indexable	    ✅ Yes (can use list[0])	    ✅ Yes	                    ❌ No (not indexable)
# Duplicates	✅ Allowed	                ✅ Allowed	                ❌ Not allowed (unique items)
# Use cases	    General-purpose, editable	  Fixed collections	           Unique items, fast lookups
# Syntax	    [1, 2, 3]	                  (1, 2, 3)	                   {1, 2, 3} or set()


# -------------------------------------------------------------------------
# List: 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# print(dir(list))

# my_list = ['red', 'blue', 'green', 30, 50, True, False, None]
# print(my_list[-1])
# print(my_list[:4])
# print(my_list[::-1])

list_1 = [1,2,3,4,5,8,0]
list_2 = [5,6,7,8,9]

# list_3 = list_1 + list_2
# print(list_3)

# list_1.extend(list_2)
# print(list_1)

# list_1.append('six')    # pass the value which should be append        
# print(list_1)

# list_1.clear()
# print(list_1) 

# print(list_1.count(5))
# list_1.insert(5, 100)
# print(list_1)

# list_1.reverse()
# print(list_1)

# list_1.sort(reverse= True)
# print(list_1)
            
# poped_value = list_1.pop()              # removes sp-ecific index from list, default -1
# print(list_1.pop(4), list_1)            # list_1 = [1,2,3,4,5]

# list_1.remove(8)                        # removes value from list
# print(list_1)                   


# -------------------------------------------------------------------------
# Tuples: 'count', 'index'
# print(dir(tuple))

# my_tup = (1,2,3,4,5,1)
# sec_tup = (2,3) + my_tup
# print(my_tup + sec_tup)

# -------------------------------------------------------------------------
# Set: 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
# print(dir(set))

# set_1 = {1,2,3,5,7,7,3,1,2}
# print(set_1)
# set_2 = {3,5,7}

# union_of_set = set_1.intersection(set_2)
# print(set_2.issubset(set_1))

# -------------------------------------------------------------------------
# my_list = [1,2,3,4,1,5]
# my_tup = tuple(my_list)
# my_set = set(my_list)

# print(my_set)
# print(list(set(my_list)))
