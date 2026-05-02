from math import gcd


# ================= HELPERS =================
def clean_text(text):
    return text.upper() if text else ""


def is_valid_key(key):
    return key and any(c.isalpha() for c in key)


# ================= CAESAR =================
def caesar_encrypt(text, shift):
    if not text:
        return ""

    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ================= VIGENERE =================
def vigenere_encrypt(text, key):
    if not text or not is_valid_key(key):
        return text

    key = "".join([c for c in key.lower() if c.isalpha()])
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result


def vigenere_decrypt(text, key):
    if not text or not is_valid_key(key):
        return text

    key = "".join([c for c in key.lower() if c.isalpha()])
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 97
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base - shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result


# ================= PLAYFAIR =================
def create_matrix(key):
    key = clean_text(key).replace("J", "I")
    seen = set()
    matrix = []

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix.append(ch)

    return [matrix[i*5:(i+1)*5] for i in range(5)]


def find_pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def build_pairs(text):
    text = clean_text(text).replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                filler = "X" if a != "X" else "Q"
                pairs.append((a, filler))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, "X"))
            i += 1

    return pairs


def playfair_encrypt(text, matrix):
    pairs = build_pairs(text)
    result = ""

    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def playfair_decrypt(text, matrix):
    if len(text) % 2 != 0:
        return ""

    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# ================= RAIL FENCE =================
def rail_encrypt(text, rails):
    if not text or rails <= 1 or rails >= len(text):
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for ch in text:
        fence[rail].append(ch)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join("".join(r) for r in fence)


def rail_decrypt(cipher, rails):
    if not cipher or rails <= 1 or rails >= len(cipher):
        return cipher

    pattern = [['' for _ in range(len(cipher))] for _ in range(rails)]

    rail = 0
    direction = 1

    for i in range(len(cipher)):
        pattern[rail][i] = '*'
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pattern[r][c] == '*':
                pattern[r][c] = cipher[index]
                index += 1

    result = ""
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        result += pattern[rail][i]
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    return result


# ================= ROT13 =================
def rot13(text):
    if not text:
        return ""
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + 13) % 26 + base)
        else:
            result += ch
    return result


# ================= COLUMNAR =================
def col_encrypt(text, key):
    if not text or not key or len(key) < 2:
        return text

    cols = len(key)
    grid = ['' for _ in range(cols)]

    for i, ch in enumerate(text):
        grid[i % cols] += ch

    key_order = sorted([(k, i) for i, k in enumerate(key)],
                       key=lambda x: (x[0], x[1]))

    result = ""
    for _, i in key_order:
        result += grid[i]

    return result


def col_decrypt(cipher, key):
    if not cipher or not key or len(key) < 2:
        return cipher

    cols = len(key)
    rows = len(cipher) // cols
    extra = len(cipher) % cols

    key_order = sorted([(k, i) for i, k in enumerate(key)],
                       key=lambda x: (x[0], x[1]))

    grid = [''] * cols
    index = 0

    for pos, (_, col) in enumerate(key_order):
        length = rows + (1 if pos < extra else 0)
        grid[col] = cipher[index:index + length]
        index += length

    result = ""
    for i in range(rows + (1 if extra else 0)):
        for j in range(cols):
            if i < len(grid[j]):
                result += grid[j][i]

    return result


# ================= HILL =================
def matrix_mod_inv(matrix, mod=26):
    a, b = int(matrix[0][0]), int(matrix[0][1])
    c, d = int(matrix[1][0]), int(matrix[1][1])

    det = (a * d - b * c) % mod

    if gcd(det, mod) != 1:
        raise ValueError("Matrix not invertible mod 26")

    det_inv = pow(det, -1, mod)

    adj = [
        [d, -b],
        [-c, a]
    ]

    return [
        [(det_inv * adj[0][0]) % mod, (det_inv * adj[0][1]) % mod],
        [(det_inv * adj[1][0]) % mod, (det_inv * adj[1][1]) % mod]
    ]


def hill_encrypt(text, key_matrix):
    text = clean_text(text).replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - 65
        p2 = ord(text[i+1]) - 65
        
        c1 = (key_matrix[0][0] * p1 + key_matrix[0][1] * p2) % 26
        c2 = (key_matrix[1][0] * p1 + key_matrix[1][1] * p2) % 26
        
        result += chr(int(c1) + 65) + chr(int(c2) + 65)

    return result


def hill_decrypt(text, key_matrix):
    inv = matrix_mod_inv(key_matrix)

    result = ""

    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - 65
        c2 = ord(text[i+1]) - 65
        
        p1 = (inv[0][0] * c1 + inv[0][1] * c2) % 26
        p2 = (inv[1][0] * c1 + inv[1][1] * c2) % 26
        
        result += chr(int(p1) + 65) + chr(int(p2) + 65)

    return result
