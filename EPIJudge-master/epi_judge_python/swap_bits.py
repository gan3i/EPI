from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    if (x >> i) & 1 != (x >> j) & 1:

        bit_mask = (1 << i) | (1 << j)
        return x ^ bit_mask
    return x

#  print(swap_bits(1, 64, 1))

# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
#                                        swap_bits))
