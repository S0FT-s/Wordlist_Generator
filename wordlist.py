##########################
#      By S0FT-s         #                    
##########################

import itertools
import colorama
from colorama import Fore, Back 
colorama.init(autoreset=True)


File_path = ''
info = ['0','1','2','3','4','5','6','7','8','9']
info_c = []
passlen = 0

print(Fore.BLUE +"""                                                                                                                           

 _      __            ____   _     __   
 | | /| / /__  _______/ / /  (_)__ / /_  
 | |/ |/ / _ \/ __/ _  / /__/ (_-</ __/  
 |__/|__/\___/_/  \_,_/____/_/___/\__/   
 / ___/__ ___  ___ _______ _/ /____  ____
/ (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
\___/\__/_//_/\__/_/  \_,_/\__/\___/_/

By:S0FT-s                                         
GitHub: https://github.com/S0FT-
""")

File_path = input("What is the path to the file where you want to save the wordlist?\n-->")
pathf = open(File_path, 'w')

passlen = int(input("what is the maximum password length\n-->"))
print("------------------------------------------------------")
range1 = int(input("how many info you wnat to put? ex: 8\n-->"))

opt = int(input("""what type numbers you want?
1] customized
2] prefix 0 to 9
"""))

if(opt == 1):
    for q in range(range1):
        info.append(input("target info\t\t-->"))
        pass



elif(opt == 2):
    for q in range(range1):
        info_c.append(input("target info\t\t-->"))
        pass


else:
    print(Fore.RED+"Invalid option")


op = int(input("""what type of spaces you what?
1] customized
2] all ex: - _ 
"""))


if(op == 1):
    espaco =(input("What type of spaces you want ex: - _ if you want a blank space leave blank "))
    for i in itertools.product(info,info_c, repeat=passlen):
        pathf.write(espaco.join(i) + "\n")

    print(Fore.GREEN +"all passwords generated successfully passwords generate")



elif(op == 2):
    for i in itertools.product(info,info_c, repeat=passlen):
        pathf.write("".join(i) + "\n")
        pathf.write("_".join(i) + "\n")
        pathf.write("-".join(i) + "\n")

    print(Fore.GREEN +"all passwords generated successfully passwords generate ")

else:
    print(Fore.RED+"Invalid option")
