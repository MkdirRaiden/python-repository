name=['rose', 'raiden', 'helen', 'arslan']
new_name=[x.capitalize() for x in name]
gender=['F', 'M', 'F', 'M']
age=[21, 26, 23, 25]
z=zip(new_name, gender, age)
for new_name, gender, age in z:
    print('%s gender is %s and his age is %d' %(new_name, gender, age))