import kociemba


col = "YLRLLOGGYRBGGRBYBBOYBOGRBYGLBOGYRGYLBRLROLROOYGOLBYROL"
col = "YBLRLOYOOGLRBROGRRGYYOGLBGLLYORYYYRLRGRLOGOLOBYBBBGGBB"
col = "YLRRLBBGLGOYGRYRRGLROGGLOOBYLLGYBGBRGYOOOYOOBBRRBBYLLY"
col = "ORYLLGROBOOBRROOYRGYYYGYOBLGRBBYGLLGLGLROBROYRLGLBGYBB"
col = "LGYRLRRRLBYGORYGOBGBRRGGLYYOBRLYBBYYGGLLOLRBBOLOOBOOGY"
col = "GBOLLLROGLGBLRGOYYBBRYGOYYLGOBOYBBBGORYRORLGRYLLYBGORR"
col = "BRRBLLLYOGRGBRLGGLBGYBGYBOLLYOGYLROGOORLORYROYYYOBBRGB"
col = "RLBRLROYGRBOGRGLYBGOYBGYLBOROGGYRROYLLYOOYYLGLBBRBLOGB"
col = "OGBLLROBBYBYYRRLOYGORBGGBYGRRRYYLOGRLRYYOLLOLOOGGBBGLB"
col = "YBOYLBYLGLRGYRYLOBRRRLGRYGROOBGYYOROGGBOOOBLGLLRBBBLGY"
col = "LLLLLLLLLRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB"
col = "GYBLLLRYGRGLORBOOLBBYGGBYRGBGLRYLOOGYRYBOYLYOROOLBRRGB"











colors = list(col)
print '\n',colors,'\n'

for i in range(54):
    if colors[i] == 'Y':
        colors[i] = 'D'

    elif colors[i] == 'O':
        colors[i] = 'L'

    elif colors[i] == 'G':
        colors[i] = 'F'

    elif colors[i] == 'L':
        colors[i] = 'U'
        

print '1 - ',''.join(colors),'\n'

myfile = open("file.txt","w")
myfile.write(''.join(colors))
myfile.close()
		 
myfile = open('file.txt','r')
cols = myfile.read()
myfile.close()

print '2 - ',cols,'\n'
print 'rondom = ',kociemba.solve\
      ('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB',cols),'\n'
print 'solve  = ',kociemba.solve(cols),'\n'

rondom = list(kociemba.solve\
             ('UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB',cols))
solve = list(kociemba.solve(cols))

for i in range(rondom.count(' ')):
        rondom.remove(' ')


for i in range(solve.count(' ')):
        solve.remove(' ')

rondom.append('#')
solve.append('#')

rand = []
sol = []

for i in range(len(rondom)):
    if (rondom[i] == "'") or (rondom[i] == '2')or (rondom[i] == ' '):
        continue
    elif rondom[i] == "#":
        break

    elif rondom[i] == 'U':
        if rondom[i+1] == "'":
            rand.append('u')
        elif rondom[i+1] == "2":
            rand.append('5')
        else:
            rand.append(rondom[i])
            
    elif rondom[i] == 'R':
        if rondom[i+1] == "'":
            rand.append('r')
        elif rondom[i+1] == "2":
            rand.append('0')
        else:
            rand.append(rondom[i])

            
    elif rondom[i] == 'D':
        if rondom[i+1] == "'":
            rand.append('d')
        elif rondom[i+1] == "2":
            rand.append('1')
        else:
            rand.append(rondom[i])



    elif rondom[i] == 'L':
        if rondom[i+1] == "'":
            rand.append('l')
        elif rondom[i+1] == "2":
            rand.append('2')
        else:
            rand.append(rondom[i])


    elif rondom[i] == 'B':
        if rondom[i+1] == "'":
            rand.append('b')
        elif rondom[i+1] == "2":
            rand.append('3')
        else:
            rand.append(rondom[i])
    elif rondom[i] == 'F':
        if rondom[i+1] == "'":
            rand.append('f')
        elif rondom[i+1] == "2":
            rand.append('4')
        else:
            rand.append(rondom[i])

for i in range(len(solve)):
    if (solve[i] == "'") or (solve[i] == '2'):
        continue
    elif solve[i] == "#":
        break

    elif solve[i] == 'U':
        if solve[i+1] == "'":
            sol.append('u')
        elif solve[i+1] == "2":
            sol.append('5')
        else:
            sol.append(solve[i])
        
    elif solve[i] == 'R':
        if solve[i+1] == "'":
            sol.append('r')
        elif solve[i+1] == "2":
            sol.append('0')
        else:
            sol.append(solve[i])
    elif solve[i] == 'D':
        if solve[i+1] == "'":
            sol.append('d')
        elif solve[i+1] == "2":
            sol.append('1')
        else:
            sol.append(solve[i])



    elif solve[i] == 'L':
        if solve[i+1] == "'":
            sol.append('l')
        elif solve[i+1] == "2":
            sol.append('2')
        else:
            sol.append(solve[i])


    elif solve[i] == 'B':
        if solve[i+1] == "'":
            sol.append('b')
        elif solve[i+1] == "2":
            sol.append('3')
        else:
            sol.append(solve[i])


    elif solve[i] == 'F':
        if solve[i+1] == "'":
            sol.append('f')
    
        elif solve[i+1] == "2":
            sol.append('4')
        else:
            sol.append(solve[i])
            
rondom.remove('#')
solve.remove('#')

rand = ''.join(rand)
sol = ''.join(sol)
print "rondom = ",rand,'\n'
print "solve =  ",sol,'\n'



myfile = open("file.txt","w")
myfile.write("rondom = ")
myfile.write(rand)
myfile.write('\n\r')
myfile.write("solve =  ")
myfile.write(sol)
myfile.close()



    

