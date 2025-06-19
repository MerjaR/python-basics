# Working with classmethods
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counts = {}
        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        
        most_common = None
        highest_count = 0

        for item, count in counts.items():
            if count > highest_count:
                highest_count = count
                most_common = item
        
        return most_common

    @classmethod
    def doubles(cls, my_list:list):
        counts = {}
        for item in my_list:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        
        count_of_doubles = 0
        for key in counts:
            if counts[key] >= 2:
                count_of_doubles += 1
                
        return count_of_doubles


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
