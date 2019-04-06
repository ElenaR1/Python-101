
import sys
# s={x for x in range(10) if x%2==0}
# print(s)# set-a nqma indeksi ili podredba

# s1={x: x**2 for x in range(10) if x%2==0}
# print(s1)

def hangman(clue_word):
    n=len(clue_word)
    count=0
    count_errors=0
    flag=True
    msg='Guess a letter:'
    dashes=[]
    for i in range(n):
        dashes.append('_')
    print(dashes)
    s=' '.join(dashes)
    print(s)
    while flag :
        print(msg)
        letter = input()
        if clue_word.find(letter)==-1:
            print('Incorrect!')
            count_errors+=1
        if clue_word.find(letter)!=-1:
            #index=clue_word.find(letter)
            #print('index',index)
            for i in range(n):
                if clue_word[i]==letter:
                    dashes[i]=letter
            #dashes[index]=letter
            print(' '.join(dashes))
            count+=1 
        # if ' '.join(dashes).find(letter)!=-1:
        #     found=' '.join(dashes).find(letter)
        #     index=clue_word.find(letter,found)
        #     print('index',index)
        #     dashes[index]=letter
        #     print(' '.join(dashes))
        #     count+=1
        if ' '.join(dashes).find('_')==-1:
            print('congratulations you won')
            break
        if count_errors==5:
            print('you lost')
            print(" ___________")
            print("|     |     |")
            print("|   \ O /   |")
            print("|     |     |")
            print("|     |     |")
            print("|    / \    |")
            print("|           |")
            flag=False
            

def main():
    print('Welcome to Hangman! Let\'s play!')
    hangman(sys.argv[1])

if __name__=='__main__':
    main()
    

