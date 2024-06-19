hobbies = ['Drawing', 'Reading', 'Watching', 'Writing']
fav_subjects = ['Programming', 'English', 'Math', 'Science']
fav_numbers = [4, 9, 10, 5, 6, 2]

hobbies.append('Procastinating')
hobbies.sort()
fav_subjects.reverse()
fav_subjects.insert(1, 'Pentesting')
fav_numbers.pop(0)

print(fav_subjects + hobbies)
print(fav_numbers)