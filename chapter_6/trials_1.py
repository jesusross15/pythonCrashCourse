people = {
    'zander': ['zander', 'marenberg', 22, "new providence"], 
    'aaron': ['aaron', 'eisen', 22, "edison"],
    'jesus': ['jesus', 'ross', 22, 'jersey city'],
}

for name, details in people.items():
    print(f"These are the details of {name.title()}:")
    for detail in details:
        print(f"\t{detail}")
