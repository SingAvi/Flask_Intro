expertise = ["Android", "Python", "UI | UX Designing"]
expertise_list = "<ul>"
expertise_list += "\n".join(["<li>{expert}</li>".format(expert=expert) for expert in expertise])
expertise_list += "<ul>"
print(expertise_list)