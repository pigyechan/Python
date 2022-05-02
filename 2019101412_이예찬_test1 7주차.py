animal=["dog", "duck", "pony", "donkey", "giraffe", "elephant", "cat"]

print("[실행 결과]\n\n")
for i in animal:
    if len(i) <= 5:
        print(f"\t{i}")
        print()
    else:
        continue
