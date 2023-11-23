#Nesting List inside Dictionary, later printing the content inside the list.

items = {'Name':'Saraswati','Other Names': ['Brahmi','ManiPrabha','HamsaVahani','Vani','Vidya']}

print(f"Her Name is {items['Name']},She is also called by the following names")

for many_names in items['Other Names']:
    print(f"\t{many_names}")
