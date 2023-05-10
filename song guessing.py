import fontstyle  # pip install fontstyle
from threading import Timer
import random

def baka(): 
    timeout = 30
    t = Timer(timeout, print, ['\n Sorry, times up \n please type exit()'])
    t.start()
    prompt ="\n your answer--> "
    answer = input(prompt)
    t.cancel()
    return answer

def eng(): #english options
    ans=("(a) shape of you      (b) perfect         (c) baby      (d) at my worst       (e)night changes\n")
    print(ans)

def hindi(): #hindi options
    ans2=("""(a) Muzko rana ji maaf karna          (b) Tum hi ho         (c)hum tum ek kamre mein band ho    
(d)Badtameez dil                      (e)Apna bana le \n""")
    print(ans2)


title = ("SILLY SONG SINGS")
x = title.center(130)
print(fontstyle.apply(x, 'bold/red'))

print("Are You Ready?")
y = "[Yes]        ['No' can't be your option]"
print(y)
n = input() 
z = "yes" ; a = "Yes" ; b = "no" ; c = "No"

if n == z or n == a or n == b or n == c:
    print()
    print(fontstyle.apply("START THE GAME", 'bold'))
    print(fontstyle.apply("Guess 'Hindi' song or 'English' song", 'bold/cyan/italic'))
    x = input()
    a = "Hindi" ; d = "hindi" ; e = "english" ; b = "English"
#hindi
    if x == a or x == d:
        ca = (fontstyle.apply("Hindi", 'bold/green'))
        print("you have selected", ca, "song")
        print()
        a = (fontstyle.apply("Rules-->", 'bold/red'))
        print(a, fontstyle.apply("\n you have 30 seconds to guess \n have fun!",'bold'))

    #songs 
        b1="""My brother in law was sleeping on roof, I slept with him in mistaken of you, I am sorry rana ji mitake is being done by me.""" # Muzko rana ji maaf karna

        b2="""Now I can't live without you
Without you, what is my worth ? 
I can't live without you
Without you, what is my worth ?
May be if i seperated from you 
Then I'll get seperated from myself
Because you are the one
Now you are the only one. 
You are my world
My peace and my pain
You alone are my love""" # Tum hi ho

        b3="""Nobody can come in from the outside
Nobody can go out from the inside
Think, what would happen in a situation...
Think, what would happen in such a situation...
You and I.......
Are both locked in a room....
And the key is lost...
Then I will get lost in the charm of your eyes!
You and I ....
Are both locked in a room and the key is lost ....""" # hum tum ek kamre mein band ho

        b4="""I've seen mint in the betel leaf 
I've seen the gem on your nose ring 
I've seen a beautiful girl
And A Handsome rascal
The moon became a cheater and cheated
So all the stars said , gili gili akkha
Some spirit has taken over it and doesn't know how to stop
Now it can't even tell the difference between right and wrong
It's stuck to stubbornness and doesn't let go
Bad mannered heart, bad mannered heart , bad mannered heart
Doesn't heed
Doesn't heed""" # Badtameez dil

        b5="""We are not related to each other but still there's some connection between us
Whatever you did how did you do that 
Like you have tied my heart
I can't even understand this
You are like my morning sunshine
We are not related to eachother but still there's some connection between us
Make me yours ,
O Beloved,
Make me yours
Set up a city in the valley of hearts, o Beloved""" # Apna bana le
        ran0=random.choice([b1,b2,b3,b4,b5])
        print(ran0)
    #mcq logic code
        if ran0==b1:
            hindi()
            bake=baka()
            if bake=="a":
                print("hurray!")

        elif ran0==b2:
            hindi()
            bake=baka()
            if bake=="b":
                print("hurray!") 
            else:
                print("try again")

        elif ran0==b3:
            hindi()
            bake=baka()
            if bake=="c":
                print("hurray!")
            else:
                print("try again")

        elif ran0==b4:
            hindi()
            bake=baka()
            if bake=="d":
                print("hurray!")
            else:
                print("try again")

        elif ran0==b5:
            hindi()
            bake=baka()
            if bake=="e":
                print("hurray!")
            else:
                print("try again")

#english
    elif x == b or x == e:
        cb = (fontstyle.apply("English", 'bold/green'))
        print("you have selected", cb, "song")
        print()
        a = (fontstyle.apply("Rules-->", 'bold/red'))
        print(a, fontstyle.apply("\n you have 30 seconds to guess \n have fun!",'bold'))
        print()

    #songs
        a1='''ladakee, tumhen pata hai ki mujhe tumhaara pyaar chaahie
aapaka pyaar mere jaise kisee ke lie hastanirmit tha
ab chalo, mere netrtv ka paalan karen
main paagal ho sakata hoon, mujhe bura mat maanana
bol beta, jyaada baat mat karo
meree kamar ko pakad lo aur us shareer ko mujh par daal do
ab chalo, mere netrtv ka paalan karen
aao, ab aao, mere netrtv ka paalan karo
mujhe aap ke aakaar se pyaar hai
ham chumbak kee tarah dhakka dete hain aur kheenchate hain
haalaanki mera dil bhee gir raha hai
mujhe tumhaare shareer se pyaar hai''' #shape of you
        
        a2='''bebee, main andhere mein naach raha hoon
tumhaare saath meree baahon ke beech
ghaas par nange pair
hamaara pasandeeda gaana sun rahe hain
jab aapane kaha ki aap gadabad dikh rahe hain
main apanee saans ke neeche phusaphusaaya
lekin aapane suna
daarling, tum aaj raat ekadam sahee lag rahee ho''' #perfect
        
        a3='''tumhen pata hai ki tum mujhase pyaar karate ho , mujhe pata hai ki tum paravaah karate ho 
bas jab bhee chillao , aur main vahaan rahoonga
tum mere pyaar ho , tum mere dil ho 
aur ham kabhee, kabhee, kabhee alag nahin honge''' #baby
        
        a4='''mujhe kisee aise vyakti kee aavashyakata hai jo mujhe mere sabase bure samay mein pyaar kar sake
nahin, main sampoorn nahin hoon, lekin mujhe aasha hai ki aap meree yogyata dekhenge
kyonki yah keval tum ho, koee naya nahin, mainne tumhen sabase pahale rakha
aur tumhaare lie, ladakee, main kasam khaata hoon ki main sabase bura karoonga''' #at my worst 
        
        a5='''ham keval bade ho rahe hain, bebee
aur main isake baare mein haal hee mein soch raha hoon
kya yah aapako kabhee paagal kar deta hai
raat kitanee tejee se badalatee hai?
vah sab kuchh jo aapane kabhee sapana dekha hai
jaagane par gaayab ho jaana
lekin darane kee koee baat nahin hai
bhale hee raat badal jae
yah mujhe aur aapako kabhee nahin badalega'''  #night changes
        ran=random.choice([a1,a2,a3,a4,a5])
        print(ran)
    #mcq logic code
        if ran==a1:
            eng()
            ne=baka()
            if ne=="a":
                print("hurray!")
            else:
                print("try again")

        elif ran==a2:
            eng()
            ne=baka()
            if ne=="b":
                print("hurray!")
            else:
                print("try again")

        elif ran==a3:
            eng()
            ne=baka()
            if ne=="c":
                print("hurray!")
            else:
                print("try again")

        elif ran==a4:
            eng()
            ne=baka()
            if ne=="d":
                print("hurray!")
            else:
                print("try again")

        elif ran==a5:
            eng()
            ne=baka()
            if ne=="e":
                print("hurray!")
            else:
                print("try again")
<<<<<<< HEAD
#end
=======
<<<<<<< HEAD

#kuchbe
=======
#end
>>>>>>> 7b4065d (added read.md)
>>>>>>> 86bfa6268c262e0beb35599e74d7ab97ca42142c
