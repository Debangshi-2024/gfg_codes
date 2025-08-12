arr = []

def insert(value):
    arr.append(value)

def delete(value):
    if value in arr:
        arr.remove(value)

def search(value):
    return value in arr

def display():
    print("Array:", arr)

while True:
    print("\n1.Insert  2.Delete  3.Search  4.Display  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        insert(int(input("Enter value to insert: ")))
    elif ch == 2:
        delete(int(input("Enter value to delete: ")))
    elif ch == 3:
        print("Found" if search(int(input("Enter value to search: "))) else "Not Found")
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
