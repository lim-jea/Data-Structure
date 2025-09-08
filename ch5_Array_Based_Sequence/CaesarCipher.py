def insertion_sort(A):
    """Sort array of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        cur = A[k]                                # current element to be inserted
        j = k                                     # find correct index j for cur
        while j > 0 and A[j - 1] > cur:          # thus, A[j-1] must go after cur
            A[j] = A[j - 1]                       # slide element A[j-1] to the right
            j -= 1
        A[j] = cur                                # cur is now in the correct place
        
class CaesarCipher:
    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for alphabet."""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        """Return string representing encryoted message."""
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        """Return string representing decrypted message."""
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]
        return ''.join(msg)
    
if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = 'THE EAGLE IS IN PLAY; MEET AT JOE\'S.'
    coded = cipher.encrypt(message)
    print('\nSecret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)