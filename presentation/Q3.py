    # 3. Take a dictionary of 4 items ,key shud be int and values shud be string and print only values associated with even keys
    
dic={1:"jatin",2:"heer",4:"manihs",5:"jstin",6:"sneha"}
for k,v in dic.items():
    if(k%2==0):
        print(k,v)
        
