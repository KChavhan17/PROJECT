#Skill set matcher
def match_skills(required, candidate):
    matched = required & candidate
    missing = required - candidate
    return matched, missing

required_skills = {"Python", "SQL", "Excel", "Communication", "Git"}

candidate1 = {"Python", "Excel", "PowerBI", "Communication"}
candidate2 = {"Java", "SQL", "Git", "HTML"}

match1, miss1 = match_skills(required_skills, candidate1)
print("Candidate 1")
print("Matched Skills:", match1)
print("Missing Skills:\n", miss1)

match2, miss2 = match_skills(required_skills, candidate2)
print("Candidate 2")
print("Matched Skills:", match2)
print("Missing Skills:", miss2)