# Copyright 2010, David S. Bolme, Colorado State University Research 
# Foundation
#
# Colorado State University Software Evaluation License Agreement
#
# This license agreement ("License"), effective today, is made by and between 
# you (hereinafter referred to as the "Licensee") and the Board of Governors of 
# the Colorado State University System acting by and through Colorado State 
# University, an institution of higher education of the State of Colorado, 
# located at Fort Collins, Colorado, 80523-2002 ("CSU"), and concerns certain 
# software described as "Correlation Filters for Detection, Recognition, and 
# Registration," a system of software programs for advanced video signal 
# processing and analysis. 
#
# 1.  General. A non-exclusive, nontransferable, perpetual license is granted 
#     to the Licensee to install and use the Software for academic, non-profit, 
#     or government-sponsored research purposes. Use of the Software under this 
#     License is restricted to non-commercial purposes. Commercial use of the 
#     Software requires a separately executed written license agreement. 
#    
# 2.  Permitted Use and Restrictions. Licensee agrees that it will use the 
#     Software, and any modifications, improvements, or derivatives to the 
#     Software that the Licensee may create (collectively, "Improvements") 
#     solely for internal, non-commercial purposes and shall not distribute, 
#     transfer, deploy, or externally expose the Software or Improvements to any 
#     person or third parties without prior written permission from CSU. The 
#     term "non-commercial," as used in this License, means academic or other 
#     scholarly research which (a) is not undertaken for profit, or (b) is not 
#     intended to produce works, services, or data for commercial use, or (c) is 
#     neither conducted, nor funded, by a person or an entity engaged in the 
#     commercial use, application or exploitation of works similar to the 
#     Software. 
#    
# 3.  Ownership and Assignment of Copyright. The Licensee acknowledges that 
#     CSU has the right to offer this copyright in the Software and associated 
#     documentation only to the extent described herein, and the offered 
#     Software and associated documentation are the property of CSU. The 
#     Licensee agrees that any Improvements made by Licensee shall be subject 
#     to the same terms and conditions as the Software. Licensee agrees not to 
#     assert a claim of infringement in Licensee copyrights in Improvements in 
#     the event CSU prepares substantially similar modifications or derivative 
#     works. The Licensee agrees to use his/her reasonable best efforts to 
#     protect the contents of the Software and to prevent unauthorized 
#     disclosure by its agents, officers, employees, and consultants. If the 
#     Licensee receives a request to furnish all or any portion of the Software 
#     to a third party, Licensee will not fulfill such a request but will refer 
#     the third party to the CSU Computer Science website 
#     http://www.cs.colostate.edu/~vision/ocof.html so that the third party's 
#     use of this Software will be subject to the terms and conditions of this 
#     License. Notwithstanding the above, Licensee may disclose any 
#     Improvements that do not involve disclosure of the Software. 
#     
# 4.  Copies. The Licensee may make a reasonable number of copies of the 
#     Software for the purposes of backup, maintenance of the Software or the 
#     development of derivative works based on the Software. These additional 
#     copies shall carry the copyright notice and shall be controlled by this 
#     License, and will be destroyed along with the original by the Licensee 
#     upon termination of the License. 
#     
# 5.  Acknowledgement. Licensee agrees that any publication of results obtained 
#     with the Software will acknowledge its use by an appropriate citation as 
#     specified in the documentation. 
#     
# 6.  Acknowledgment. CSU acknowledges that the Software executes patent pending 
#     Algorithms for the purpose of non-commercial uses. Licensee acknowledges 
#     that this Agreement does not constitute a commercial license to the 
#     Algorithms. Licensee may apply for a commercial license to the Algorithms 
#     from Colorado State University Research Foundation by visiting 
#     http://www.csuventures.org. 
#    
# 7.  Disclaimer of Warranties and Limitation of Liability. THE SOFTWARE IS 
#     PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#     INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
#     AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. CSU MAKES NO 
#     REPRESENTATION OR WARRANTY THAT THE SOFTWARE WILL NOT INFRINGE ANY PATENT 
#     OR OTHER PROPRIETARY RIGHT. IN NO EVENT SHALL CSU BE LIABLE FOR ANY 
#     DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
#     (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
#     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
#     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
#     LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY 
#     OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF 
#     SUCH DAMAGE. 
#     
# 8.  Termination. This License is effective until terminated by either party. 
#     Your rights under this License will terminate automatically without notice 
#     from CSU if you fail to comply with any term(s) of this License. Upon 
#     termination of this License, you shall immediately discontinue all use of 
#     the Software and destroy the original and all copies, full or partial, of 
#     the Software, including any modifications or derivative works, and 
#     associated documentation. 
#    
# 9.  Governing Law and General Provisions. This License shall be governed by 
#     the laws of the State of Colorado, excluding the application of its 
#     conflicts of law rules. This License shall not be governed by the United 
#     Nations Convention on Contracts for the International Sale of Goods, the 
#     application of which is expressly excluded. If any provisions of this 
#     License are held invalid or unenforceable for any reason, the remaining 
#     provisions shall remain in full force and effect. This License is binding 
#     upon any heirs and assigns of the Licensee. The License granted to 
#     Licensee hereunder may not be assigned or transferred to any other person 
#     or entity without the express consent of the Regents. This License 
#     constitutes the entire agreement between the parties with respect to the 
#     use of the Software licensed hereunder and supersedes all other previous 
#     or contemporaneous agreements or understandings between the parties, 
#     whether verbal or written, concerning the subject matter. 


'''
Created on Sep 16, 2010

@author: bolme
'''

import pyvision as pv
from pyvision.types.Video import Video
import ocof
import os.path
import cv
import time
import copy

TAZ_FILENAME = os.path.join(ocof.__path__[0],'test','data','capture1.mp4')
global TAZ_RECT
TAZ_RECT = pv.Rect(200,200,120,120)

# print TAZ_FILENAME
video = pv.Video(TAZ_FILENAME)
webcam = pv.Webcam()

tracker = None

global startPointx   
global startPointy   
global flagDraw   
global src
startPointx = 0  
startPointy = 0  
flagDraw = False

def onMouseEvent(event,x,y,flags,param):  
    global startPointx   
    global startPointy   
    global flagDraw    
    # print event
    if(event==1):  
        print "Position is: %d,%d" ,x,y   
        startPointx = x  
        startPointy = y  
        flagDraw = True  
    if(event==0):  
        if(flagDraw==True):  
            image = cv.CloneImage(src) 
            cv.Rectangle(image, (startPointx,startPointy), (x,y), (255,0,0),3)  
            cv.ShowImage('window', image)  
             
            print "EndPosition is: %d,%d" ,x,y    
    if(event==4):  
        if(flagDraw==True):  
            image = cv.CloneImage(src)
            cv.Rectangle(image, (startPointx,startPointy), (x,y), (255,0,0),3)  
            cv.ShowImage('window', image)  
            flagDraw = False
            global TAZ_RECT
            TAZ_RECT = pv.Rect(startPointx,startPointy,x-startPointx,y-startPointy)


# ilog = pv.ImageLog()

i = 0
for frame in webcam:
    print "Processing Frame %d..."%i
    # print frame.channels
    # print isinstance(frame,cv.iplimage)
    if tracker == None:
        global src
        src = cv.CloneImage(frame.asOpenCV())
        # cv.Rectangle(src, (200,200), (320,320), (255,0,0),3)
        cv.ShowImage('window', src )
        cv.SetMouseCallback('window', onMouseEvent) 
        cv.WaitKey()
        tracker = ocof.MOSSETrack(frame,TAZ_RECT)
    else:
        start = time.time()
        tracker.update(frame)
        stop = time.time()
        print "period:",(stop-start)

        rect = tracker.rect
        print rect
        image = cv.CloneImage(frame.asOpenCV())
        cv.Rectangle(image, ((int)(rect.x),(int)(rect.y)), ((int)(rect.x+rect.w),(int)(rect.y+rect.h)), (255,0,0),2)  
        cv.ShowImage('window2', image)
        if cv.WaitKey(1) & 0xFF == ord('q'):
            break

    # cv.NamedWindow('window')
    # cv.ShowImage('window', frame.asOpenCV() )
    # cv.WaitKey()
        
    bounds = tracker.asRect()
    
    # tracker.annotateFrame(frame)
    
    # ilog(frame,format='jpg')
    i += 1
print i
    
# ilog.show()
