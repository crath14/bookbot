def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    
    #print(f"The file contains {len(file_contents)} characters.")
    print("---Begin report of books/frankenstein.txt---")
    
    words = file_contents.split()
    print(f" {len(words)} words found in the document")

    lowered_string = file_contents.lower()
    
    character_count = {}

    #for character in lowered_string:
        #current_count = character_count.get(character, 0)
        #character_count[character] = current_count + 1
    #print(character_count)
    # this will print the dictionary with all character counts 
    # including non letters

    for character in lowered_string:
        if character.isalpha():
            current_count = character_count.get(character, 0)
            character_count[character] = current_count +1
    
    char_list = []
    for char, count in character_count.items():
        char_dict ={"char":char, "count":count}
        char_list.append(char_dict)
        
        # for each character/count in the character_count dict
        #create new dict
        #then append that dictionary char and count to the list char_list
        #print(f"The {char}character was found {count} times")
    char_list.sort(key=lambda x: x['count'], reverse=True)
    #For each item (x) in the list
    #Use the value associated with the 'count' key for comparison
    #sort by highest value
    for item in char_list:
        print(f"The '{item['char']}'character was found {item['count']} times")

    print("--- End report---")
    
main()