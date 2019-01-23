###MANGO-CONFIGURE-0.0.0.4###
ver = '0123190006'
global default
default = ('MANGOCONF' + ver + '|pauseAtNextInstruction=0|autoSelectFirstFile=0|printTitle=1|printCoreSelfTestSimilarity=0')
def config_edit():
    import os
    config_list = []
    defMangoString = []
    rewritelist = []
    try:
        with open('mgsc.conf', 'r') as config:
            for number,letter in enumerate(((config.read()).split('|'))):
                if 'MANGO' in letter:
                    defMangoString.append(letter)
                    continue
                config_list.append(letter)
            config.close()
        print(config_list)
        for number,letter in enumerate(config_list):
            toChange = letter[:-1]
            chVal = input(toChange)
            try:
                chVal = int(chVal)
            except:
                print("Invalid choice, defaulting to 0")
                chVal = "0"
            try:
                if chVal >= 2:
                    print("Invalid choice, defaulting to 0")
                    chVal = "0"
            except:
                chVal = "0"
            rewrite = (toChange + str(chVal))
            rewritelist.append(rewrite)
        print("Writing changes...")
        rewritelist.insert(0, defMangoString[0])
        with open('mgsc.conf', 'w', newline='') as config:
            config.write('|'.join(rewritelist))
            config.close()
        print("Write successful.")
        print("Mango will now restart.")
        input()
        try:
            os.startfile('mango.py')
        except:
            pass
        exit()
    except:
        print("Unspecified error.")
        exit()
def config_test():
    print("Mango Config Response Successful.")
def config_init(vals):
    with open('mgsc.conf', 'w') as mgsc:
        try:
            mgsc.write(vals)
        except:
            print("Creation failed.")
        mgsc.close()
def config_call(raw):
    try:
        with open('mgsc.conf', 'r') as mgsc:
            try:
                if raw == True:
                    print(mgsc.read())
                else:
                    for number,letter in enumerate(((mgsc.read()).split('|'))):
                        if 'MANGO' in letter:
                            continue
                        print(letter)
            except:
                print("Failed to read.")
                input()
                exit()
    except:
        print("No config file.")
        print("Creating...")
        vals = default
        config_init(vals)
