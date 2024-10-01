import json

def main():
    with open("storafe_(file.json","r")as file:
        data=json.load(file)
    query=input("Enter what you want to view:\n")
    if query in data:
        print(f"your responce is {data[qery]}")
    else:
        print("The requesed responce is not present\n")


if __name__=="__main__":
    main()