
# coding: utf-8

# In[3]:


num = input("Enter comma-separated numbers : ")
list = num.split(",")
print("List : ", list)


# In[4]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[7]:


word = input("Enter a word to reverse: ")
reversestring = word[::-1];
print("Reverse String : " , reversestring)


# In[8]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t and to secure to all its citizens")

