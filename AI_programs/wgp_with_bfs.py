#wgp
cj1=5
cj2=10
targate=15

queue=["0,0"]
queue_all=["0,0"]
def heart(j1,j2):
  if j1+j2==targate:
     print(str(j1)+","+str(j2)+"exist")
     return True
   
  else:

    if str(j1)+","+str(j2) not in queue_all:
         queue.append(str(j1)+","+str(j2))
         print(str(j1)+","+str(j2))
         queue_all.append(str(j1)+","+str(j2))
         return False

def main_fun():

    while queue:
       capacity=queue[0].split(",")
       j1=int(capacity[0])
       j2=int(capacity[1])
       del queue[0]

       if heart(j1,0):
          return True
       
       if heart(0,j2):
          return True
 
       if((cj1-j1)>=j2):
         TL_j1=j1+j2
         TL_j2=0
       else:
         TL_j1=cj1
         TL_j2=j2-(cj1-j1)
       if heart(TL_j1,TL_j2):
          return True
       
       if((cj2-j2)>=j1):
         TR_j1=0
         TR_j2=j1+j2
       else:
         TR_j1=j1-(cj2-j2)
         TR_j2=cj2
       if heart(TR_j1,TR_j2):
          return True
 
       if heart(j1,cj2):
          return True
       
       if heart(cj1,j2):
          return True

       #print(queue)
    print("not found")
    return False
main_fun()
    
    

