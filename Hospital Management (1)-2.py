import pickle,os
s={}
s1=[
    {"Name": "Dr. Smith Finning", "Speciality": "Cardiology", "Availability": "Available"},
    {"Name": "Dr. Johnson Abraham", "Speciality": "Dermatology", "Availability": "Not Available"},
    {"Name": "Dr. Brown James", "Speciality": "Orthopedics", "Availability": "Available"},
    {"Name": "Dr. John Smith", "Speciality": "Pediatrics", "Availability": "Available"},
    {"Name": "Dr. Michael Johnson", "Speciality": "Neurology", "Availability": "Not Available"},
    {"Name": "Dr. David Brown", "Speciality": "Internal Medicine", "Availability": "Available"},
]
if not os.path.exists("doctors.dat"):
    with open("doctors.dat", "ab") as f:
        for i in s1:
            pickle.dump(i, f)

def Add():
    f = open("doctors.dat", "ab")
    n = int(input("Enter no. of records: "))
    for i in range(n):
        name = input("Enter doctor's name: ").strip()
        if not name.startswith("Dr. "):
            name = "Dr. " + name
        name = name.title()
        speciality = input("Enter doctor's specialty: ").capitalize()
        available = input("Enter doctor is available or not?(Available/Not Available): ").title()
        s = {"Name": name, "Speciality": speciality, "Availability": available}
        pickle.dump(s, f)
    f.close()
    
def Display():
    try:
        f = open("doctors.dat", "rb")
        print("{:<20} {:<20} {:<20}".format("Name", "Speciality", "Availability"))
        print("=" * 60)
        while True:
            try:
                x = pickle.load(f)
                name = x.get("Name", "N/A")
                speciality = x.get("Speciality", "N/A")
                availability = x.get("Availability", "N/A")
                print("{:<20} {:<20} {:<20}".format(name, speciality, availability))
            
            except EOFError:
                break
        f.close()
    except EOFError:
        print("No doctor records found.")

def Update():
    f=open("doctors.dat","rb")
    f1=open("temp.dat","wb")
    x=input("Enter doctor name to update: ").title()
    z=input("Enter doctor is available or not(Available/Not Available)?: ").title()
    try:
        while True:
            y=pickle.load(f)
            if y["Name"]==x:
                y["Availability"]=z
                pickle.dump(y,f1)
            else:
                pickle.dump(y,f1)
    except EOFError:
            pass
    f.close()
    f1.close()
    os.replace("temp.dat","doctors.dat")
    
def Search():
    f=open("doctors.dat","rb")
    x=input("Enter a name of the doctor to search: ").title()
    found=0
    try:
        while True:
            y=pickle.load(f)
            if y["Name"]==x:
                found=1
                if y["Availability"]=="Available":
                    print(x,y["Speciality"],"Doctor is available")
                elif y["Availability"]=="Not Available":
                    print(x,y["Speciality"],"Doctor is not available")
            
    except EOFError:
        if found==0:
            print("Invalid Doctor Name")
    f.close()
    
def Delete():
    f=open("doctors.dat","rb")
    f1=open("temp.dat","wb")
    x=input("Enter the doctor name to delete: ").title()
    try:
        while True:
            y=pickle.load(f)
            if y["Name"]==x:
                continue
            else:
                pickle.dump(y,f1)
    except EOFError:
        pass
    f.close()
    f1.close()
    os.replace("temp.dat","doctors.dat")

while True:
    print("")
    print("="*60)
    print("WELCOME TO MedStar Hospital Center".center(80," "))
    print("TRIVANDRUM KERALA".center(80," "))
    print("1: Add")
    print("2: Display")
    print("3: Update")
    print("4: Search")
    print("5: Delete")
    print("6: Exit")
    choice=int(input("Enter your choice"))

    if choice==1:
        Add()
    elif choice==2:
        Display()
    elif choice==3:
        Update()
    elif choice==4:
        Search()
    elif choice==5:
        Delete()
    elif choice==6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")




