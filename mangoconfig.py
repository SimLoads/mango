###MANGO-CONFIGURE-0.0.0.2###
ver = '1210180001'
global default
default = ('MANGOCONF' + ver + '|pauseAtNextInstruction=0|autoSelectFirstFile=0|printTitle=1|printCoreSelfTestSimilarity=0')
def config_edit():
    print('wah')
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
