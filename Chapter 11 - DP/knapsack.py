class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def knapsack(max_weight, items, i):
    if i == 0 or max_weight == 0:
        return 0
    if items[i].weight > max_weight:
        # Skip this item if it's overweight
        return knapsack(max_weight, items, i - 1)
    else:
        # Making Choices and take what gives max value:
        #   1. Include item[i] => Deduct weight, add value, process next item
        #   2. Not include item[i] => process next item
        return max(knapsack(max_weight - items[i].weight, items, i - 1) + items[i].value,
                   knapsack(max_weight, items, i - 1))


if __name__ == '__main__':
    my_items = [Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30)]
    print(knapsack(5, my_items, len(my_items) - 1))
