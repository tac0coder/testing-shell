#add funcs to use in shell
def listtostr(args):
  string=''
  for var in args:
    string += var
  return string
def format_table():

    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, range(format))
            print(s1)
        print('\n')
def clear():
  from os import system as cmd
  cmd('clear')
while True:
  prog=input('\x1b[6;33m'+'>>> '+'\x1b[0m')
  getothercode = ''
  othercode = []
  try:
    if prog[len(prog)-1] ==':':
      while True:
        getothercode = input('\x1b[7;40m...\t\x1b[0m ')
        if not getothercode == '':
          othercode.append(getothercode)
        else:
          for var in range(0,len(othercode)):
            othercode[var]=f"\n\t{othercode[var]}"
          print(othercode)
          try: 
            exec(prog+listtostr(othercode))
            break
          except KeyboardInterrupt or Exception as e:
            print('\x1b[6;31m'+str(e)+'\x1b[0m')
            break
  except:
    pass
      

  try: 
   exec(prog)
  except Exception as e:
    print('\x1b[6;31m'+str(e)+'\x1b[0m')