# ASCII зображення тварин
camel = r"""
The camel habitat...
___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ;!                 ! ; ;:
             : ; :               ; ; ;,
             ; ; ;             ; ; ;;
             ; ; ;           ; ; ;
             ; ; ;         ; ; ;
        _    ; ; ;       ; ; ;
         '-._; ; ;     ; ;
            '-._;     ; ;
                '-._; ;
                   '-._
Look at that!
"""

lion = r"""
The lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `,     |  ,         MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   _      dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  / `-,   `YMMMMMMMB""-'     

"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
"""

goose = r"""
The goose habitat...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
"""

bat = r"""
The bat habitat...
_________________               _________________
 ~-.                 \  |\___/|  /               .-~
     ~-.             \ / o o \ /              .-~
        >           \|  W  |/              <
       /             /~---~\                \
      /_            |       |               _\
         ~-.        |       |            .-~
            ;        \     /           i
           /___      /\   /\          ___\
                ~-. /  \_/  \ .-~
                   V         V
"""

rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y 
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
"""

# Список тварин
animals = [camel, lion, deer, goose, bat, rabbit]

# Основна програма
print("I love animals!")
print("Let's check out the animals...")

while True:
    user_input = input("Please enter the number of the habitat you would like to view (or 'exit' to quit): ")
    if user_input == "exit":
        print("See you later!")
        break
    elif user_input.isdigit():
        habitat_number = int(user_input)
        if 0 <= habitat_number < len(animals):
            print(animals[habitat_number])
        else:
            print("Invalid habitat number. Try again!")
    else:
        print("Invalid input. Please enter a number or 'exit'.")






