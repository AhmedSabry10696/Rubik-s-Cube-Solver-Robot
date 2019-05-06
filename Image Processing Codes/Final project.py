
 
from lib2 import *


pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

cv2.namedWindow('vid',cv2.WINDOW_NORMAL)

colors = ['0'] * 54
temp =['0']*9

while(True):

        
    image = cam.get_image()
    
    pygame.image.save(image, "screenshot.jpeg")
    frame = cv2.imread("screenshot.jpeg")
    frame = cv2.flip(frame,1)

    img1 = frame[y1:y2, x1:x2]
    img2 = frame[y1:y2, x3:x4]
    img3 = frame[y1:y2, x5:x6]
    img4 = frame[y3:y4, x1:x2]
    img5 = frame[y3:y4, x3:x4]
    img6 = frame[y3:y4, x5:x6]
    img7 = frame[y5:y6, x1:x2]
    img8 = frame[y5:y6, x3:x4]
    img9 = frame[y5:y6, x5:x6]

    temp[0] = get_color(img1)
    temp[1] = get_color(img2)
    temp[2] = get_color(img3)
    temp[3] = get_color(img4)
    temp[4] = get_color(img5)
    temp[5] = get_color(img6)
    temp[6] = get_color(img7)
    temp[7] = get_color(img8)
    temp[8] = get_color(img9)
    
    cv2.rectangle(frame,(x,y),(x+length ,y+length),(255,0,0), 5)
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
    cv2.rectangle(frame,(x3,y1),(x4,y2),(0,255,0),3)
    cv2.rectangle(frame,(x5,y1),(x6,y2),(0,255,0),3)
    cv2.rectangle(frame,(x1,y3),(x2,y4),(0,255,0),3)
    cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),3)
    cv2.rectangle(frame,(x5,y3),(x6,y4),(0,255,0),3)
    cv2.rectangle(frame,(x1,y5),(x2,y6),(0,255,0),3)
    cv2.rectangle(frame,(x3,y5),(x4,y6),(0,255,0),3)
    cv2.rectangle(frame,(x5,y5),(x6,y6),(0,255,0),3)

    cv2.putText(frame,temp[0],(x1, y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[1],(x3, y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[2],(x5, y2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[3],(x1, y4),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[4],(x3, y4),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[5],(x5, y4),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[6],(x1, y6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[7],(x3, y6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.putText(frame,temp[8],(x5, y6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow('vid',frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('1'):
        colors[0] = temp[2]
        colors[1] = temp[1]
        colors[2] = temp[0]
        colors[3] = temp[5]
        colors[4] = temp[4]
        colors[5] = temp[3]
        colors[6] = temp[8]
        colors[7] = temp[7]
        colors[8] = temp[6]

        print colors[0:9]
        cv2.waitKey(0)
        
    elif k == ord('2'):
        colors[9] = temp[2]
        colors[10] = temp[1]
        colors[11] = temp[0]
        colors[12] = temp[5]
        colors[13] = temp[4]
        colors[14] = temp[3]
        colors[15] = temp[8]
        colors[16] = temp[7]
        colors[17] = temp[6]

        print colors[9:18]
        cv2.waitKey(0)
        
    elif k == ord('3'):
        colors[18] = temp[2]
        colors[19] = temp[1]
        colors[20] = temp[0]
        colors[21] = temp[5]
        colors[22] = temp[4]
        colors[23] = temp[3]
        colors[24] = temp[8]
        colors[25] = temp[7]
        colors[26] = temp[6]

        print colors[18:27]
        cv2.waitKey(0)
        
    elif k == ord('4'):
        colors[27] = temp[2]
        colors[28] = temp[1]
        colors[29] = temp[0]
        colors[30] = temp[5]
        colors[31] = temp[4]
        colors[32] = temp[3]
        colors[33] = temp[8]
        colors[34] = temp[7]
        colors[35] = temp[6]

        print colors[27:36]
        cv2.waitKey(0)
        
    elif k == ord('5'):
        colors[36] = temp[2]
        colors[37] = temp[1]
        colors[38] = temp[0]
        colors[39] = temp[5]
        colors[40] = temp[4]
        colors[41] = temp[3]
        colors[42] = temp[8]
        colors[43] = temp[7]
        colors[44] = temp[6]

        print colors[36:45]
        cv2.waitKey(0)
        
    elif k == ord('6'):
        colors[45] = temp[2]
        colors[46] = temp[1]
        colors[47] = temp[0]
        colors[48] = temp[5]
        colors[49] = temp[4]
        colors[50] = temp[3]
        colors[51] = temp[8]
        colors[52] = temp[7]
        colors[53] = temp[6]

        print colors[45:]
        cv2.waitKey(0)
        

cv2.destroyAllWindows()    
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
myfile.write('\n')
myfile.write("solve =  ")
myfile.write(sol)
myfile.close()
