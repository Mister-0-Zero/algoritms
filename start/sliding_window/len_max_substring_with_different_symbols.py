# Данa строкa s. Найти длину самой длинной подстроки без повторяющихся символов.
def length_of_longest_substring(s: str) -> int:
    left = 0
    max_len = 0
    seen = {}  # последний индекс каждого символа

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            # если встретили повтор внутри окна — сдвигаем левый указатель
            left = seen[ch] + 1
        seen[ch] = right
        # обновляем ответ
        max_len = max(max_len, right - left + 1)

    return max_len

res = length_of_longest_substring("sdfaaasdffffkjh")
print(res)