with open("myfile.txt") as x:
  contents=x.read()
  a=contents.split(" ")
  count=0
  for e in a:
    if e.title()=="Shrek" :
      count+=1
  print(count) 
