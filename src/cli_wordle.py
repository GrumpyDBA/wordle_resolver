import csv_helper as ch
import WordGuesser as wg

def main():

    csv_filename = 'all_fiveletterwords.csv'
    word_list = ch.read_words_from_csv(csv_filename)

    guesser = wg.WordGuesser(word_list)

    # todo - check if in word list 
    print("Intro text here todo")
    # input("Press enter to continue ")
    
    for _ in range(5):  # Repeat the process 5 times
        try:
            # Ask the user for a string

            guess = input(f"Enter word guess number {_+1}: ")
            
            wordle_response = input("Enter Wordle response in the format: \n\
                                      0 = not found(grey/black)\n\
                                      1 = correct and in place(green)\n\
                                      2 = out of place(yellow)\n")
            # TODO: validate input
            

            digits_from_wordle = [int(x) for x in str(wordle_response)]

            guesser.update_word_list_from_guess(guess, digits_from_wordle)
            


            # TODO: use the following pattern to actually merge dicts. Do in refactor
            # merged_dict = {k: [dict1[k]] + ([dict2[k]] if k in dict2 else []) if k in dict1 
            #    else [dict2[k]]
            #    for k in set(dict1) | set(dict2)}
            

            print(guesser.get_words())
            # Pass both of these to a function that will populate letter states
        

        except ValueError:
            print("Please enter a valid value.")

if __name__ == "__main__":
    main()