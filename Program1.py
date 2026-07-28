print("                Program NO 1                                           ")
name = input("Enter your name:")
usn = int(input("Enter your number:"))
Branch = input("Enter your branch:")
semester = int(input("Enter your semester:"))

sub1 = int(input("Enter your sub-semester:"))
sub2 = int(input("Enter your sub-semester:"))
sub3 = int(input("Enter your sub-semester:"))

total = sub1 + sub2 + sub3
avg = total/3
print(f"The name of the student is: {name} and his usn is {usn} the rest of his details are {Branch} : {semester} and his total  marks are in 3 subjects  {total} and his average marks are in 3 subjects are {avg}")


