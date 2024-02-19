def find_poker_hand(hand):
    ranks = []
    suits = []
    possibleRanks = []
    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == 'A':
            rank = 14
        elif rank == 'K':
            rank = 13
        elif rank == 'Q':
            rank = 12
        elif rank == 'J':
            rank = 11
        suits.append(suit)
        ranks.append(int(rank))
    # print(ranks,suits)
    sorted_ranks = sorted(ranks)
    # Royal Flush and Straight flush and Flush
    if suits.count(suits[0]) == 5:
        if (14 in sorted_ranks and 13 in sorted_ranks and 12 in sorted_ranks
                and 11 in sorted_ranks and 10 in sorted_ranks):
            possibleRanks.append(10)
        elif all(sorted_ranks[i] == sorted_ranks[i - 1] + 1 for i in range(1, len(sorted_ranks))):
            possibleRanks.append(9)
        else:
            possibleRanks.append(6)

    if all(sorted_ranks[i] == sorted_ranks[i - 1] + 1 for i in range(1, len(sorted_ranks))):
        possibleRanks.append(5)
    # creating a set for 4 of a kind
    # 33355 -- set --3,5 --- full house
    # 33335 --- set ---3,5--- four of a kind
    handUniqueValues = list(set(sorted_ranks))
    if len(handUniqueValues) == 2:
        for val in handUniqueValues:
            if sorted_ranks.count(val) == 4:
                possibleRanks.append(8)
            elif sorted_ranks.count(val) == 3:
                possibleRanks.append(7)

    # 3 of a kind and 2 pair
    if len(handUniqueValues) == 3:
        for val in handUniqueValues:
            if sorted_ranks.count(val) == 3:
                possibleRanks.append(4)
            if sorted_ranks.count(val) == 2:
                possibleRanks.append(3)

    if len(handUniqueValues) == 4:
        possibleRanks.append(2)
    if not possibleRanks:
        possibleRanks.append(1)

    # print(suits.count(suits[0]) == 5)
    pokerHandsRanks = {10: 'Royal Flush', 9: 'Straight Flush',
                       8: 'Four of a Kind', 7: 'Full House', 6: 'Flush',
                       5: "Straight", 4: 'Three of a Kind', 3: 'Two Pair',
                       2: "Pair", 1: "High Card"}

    output = pokerHandsRanks[max(possibleRanks)]
    print(hand, ':', output)

    return output


if __name__ == "__main__":
    find_poker(['AH', 'KH', "QH", 'JH', '10H'])  # Royal Flush
    find_poker(['QC', 'JC', "10C", '9C', '8C'])  # Straight Flush
    find_poker(hand=['5C', '5S', '5H', '5D', 'QH'])  # four of a kind
    find_poker(hand=['2H', '2D', '2S', '10H', '10C'])  # full house
    find_poker(hand=['2D', "KD", '7D', '6D', '5D'])  # flush
    find_poker(hand=['JC', '10H', "9C", '8C', '7D'])  # Straight Flush
    find_poker(hand=['10H', '10C', '10D', '2D', '2D'])  # three of a kind
    find_poker(hand=['KD', 'KH', '5C', '5S', '6D'])  # 2 pair
    find_poker(hand=['2D', '2S', '9C', 'KD', '10C'])  # Pair
    find_poker(hand=['KD', '5H', '2D', '10C', 'JH'])  # High Card
