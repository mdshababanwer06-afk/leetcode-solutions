class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        chars = sorted(freq, key=freq.get, reverse=True)

        return ''.join(ch * freq[ch] for ch in chars)