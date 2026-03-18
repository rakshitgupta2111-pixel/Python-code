student_data={
    "id1": {
        "Name": "Sara",
        "class": "v",
        "subject": "maths,science"
    },
    "id2": {
        "Name": "david",
        "class": "v",
        "subject": "maths,science"
    },
    "id3": {
        "Name": "david",
        "class": "v",
        "subject": "maths,science"
    },
    "id4": {
        "Name": "david",
        "class": "v",
        "subject": "maths,science"
    }
}

result={}
seen_keys=[]

for student_id,details in student_data.items():
     unique_key=(details["Name"],details["class"],details["subject"])

     if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

for k,v in result.items():
   print(k,":",v)

     