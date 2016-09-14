def gcd_eucid_algrorithm(left_hand_side, right_hand_side):
    if right_hand_side == 0:
        return left_hand_side
    else:
        return gcd_eucid_algrorithm(right_hand_side, left_hand_side % right_hand_side)


print gcd_eucid_algrorithm(24, 36);
