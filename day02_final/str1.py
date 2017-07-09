# Author: ray.zhang

age=28

while True:
    age=(input(">>>>:").strip())
    if len(age) == 0:
        continue
    elif age.isdigit():           #注意：isdigit是str的方法。
        print(age,type(age))
    else:
        break