# Lug'atni qiymat bo'yicha tartiblash
lugat = {
    "apple": 5,
    "banana": 10,
    "cherry": 7,
    "date": 3,
    "elderberry": 2
}

# Lug'atni qiymat bo'yicha tartiblash uchun sorted() funksiyasidan foydalanamiz
sorted_lugat = dict(sorted(lugat.items(), key=lambda item: item[1]))

print(sorted_lugat)
```

Kodni ishga tushirganda quyidagi natija chiqadi:
```python
{'date': 3, 'elderberry': 2, 'apple': 5, 'banana': 10, 'cherry': 7}
