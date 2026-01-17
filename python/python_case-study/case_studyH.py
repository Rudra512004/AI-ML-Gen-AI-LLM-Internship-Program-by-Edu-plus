'''
Case Study H: Sports Event Participation Summary 
Scenario: 
A sports club records data for participants in multiple events. Each participant can register for 
multiple sports. 
Problem Statement: 
Write a Python program to take inputs as (Participant_Name, [List_of_Sports]) and perform: 
1. Display participants who are taking part in both ‘Cricket’ and ‘Football’. 
2. Find the total number of unique sports being played. 
3. Create a tuple containing sports with the highest participation count.
'''
participants = {}
n = int(input("Number of participants: "))
for i in range(n):
    name = input("Name: ")
    sports = tuple(input("Sports (comma separated): ").split(","))
    participants[name] = sports

print("\nParticipants in both Cricket and Football:")
for p, s in participants.items():
    if "Cricket" in s and "Football" in s:
        print(p)

sports = set()
for s in participants.values():
    sports |= set(s)
print("Unique sports:", len(sports))

freq = {}
for s in participants.values():
    for sport in s:
        freq[sport] = freq.get(sport, 0) + 1

max_count = max(freq.values())
print("Sports with highest participation:")
for k, v in freq.items():
    if v == max_count:
        print(k)