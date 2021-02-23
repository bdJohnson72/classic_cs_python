from sys import getsizeof


class Compressed_Gene:

    def __init__(self, gene: str):
        self.bit_string = 1
        self.compress(gene)

    def compress(self, gene: str) -> int:
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b10
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
        return self.bit_string

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # exclude sentinal
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            else:
                gene += "T"
        return gene


if __name__ == "__main__":
    from sys import getsizeof

    middleOut = Compressed_Gene("ACAGGGTTTAGTAGTTGGAAT" * 1000)
    print(f'The compressed file is {getsizeof(middleOut.bit_string)} bytes')
    original = middleOut.decompress()
    print(f'The original file is {getsizeof(original)} bytes')

