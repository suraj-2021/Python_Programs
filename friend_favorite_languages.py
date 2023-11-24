#Creating a dictionariy where each key is Name of a person and each value is a list containing their favorite alnguages.

#creating a list
favorite_languages = {'Shree':['tami','telugu','sanskrit'],'Krishna':['Braj Bhasa','Avadi','Nepali'],'Govind':['Orissi','Bihari','Marathi'],'Hare':['Gujratri','Punjabi','Haryanvi','Himachali']}


for name,languages in favorite_languages.items():
    print(f"{name}'s favorite language is following:")
    for lang in languages:
        print(lang)
