# For the purposes of this problem, a score function is a pure function which takes a single number s as input and outputs another number, referred to as the score of s. Complete the best_k_segmenter function, which takes in a positive integer k and a score function score.
# best_k_segmenter returns a function that takes in a single number n as input and returns the best k-segment of n, where a k-segment is a set of consecutive digits obtained by segmenting n into pieces of size k and the best segment is the segment with the highest score as determined by score. The segmentation is right to left.
# For example, consider 1234567. Its 2-segments are 1, 23, 45 and 67 (a segment may be shorter than k if k does not divide the length of the number; in this case, 1 is the leftover, since the segmenation is right to left). Given the score function lambda x: -x, the best 2-segment is 1. With lambda x: x, the best segment is 67

def best_k_segmenter(k, score):
    """
    >>> largest_digit_getter = best_k_segmenter(1, lambda x: x)
    >>> largest_digit_getter(12345)
    5
    >>> largest_digit_getter(245351)
    5
    >>> largest_pair_getter = best_k_segmenter(2, lambda x: x)
    >>> largest_pair_getter(12345)
    45
    >>> largest_pair_getter(245351)
    53
    >>> best_k_segmenter(1, lambda x: -x)(12345)
    1
    >>> best_k_segmenter(3, lambda x: (x // 10) % 10)(192837465)
    192
    """
    partitioner = lambda x: (x // 10**k , x % 10**k)
    def best_getter(n):
        assert n > 0
        best_seg = None
        while not best_seg or n > 0:
            n, seg = partitioner(n)
            if not best_seg or score(seg) > score(best_seg):
                best_seg = seg
        return best_seg
    return best_getter
