def filledOrders(order, k):

    total = []
    result = 0
    for i in order:
        while sum(total) <= k:
            print(sum(total))
            total.append(min(order))
            print(total)
            order.remove(min(order))
            result += 1
        if min(order) > k:
            result = 0
    return result


print(filledOrders([5, 4, 6], 8))
