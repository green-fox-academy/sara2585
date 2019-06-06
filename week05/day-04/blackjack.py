def blackjack_hand_greater_than(hand_1, hand_2):
 
    def count_points(hand):
        count = 0
        for i in hand:
            if i in ['J','Q','K']:
                count += 10
        for i in hand:
            if i not in ['J','Q','K', 'A']:
                count += int(i)
        for i in hand:
            if i == 'A':
                if count + 11 > 21:
                    count += 1
                else:
                    count += 11

        return count
    count1 = count_points(hand_1)
    count2 = count_points(hand_2)
    print(count1, count2)
    if count1 > count2 and count1 <= 21:
        return True
    elif count1 < count2 and count1 <= 21 and count2 > 21:
        return True
    else:
        return False


blackjack_hand_greater_than(['J', 'A', 'A', '2'], ['9', '6', 'K', 'A', '5', 'J'])
