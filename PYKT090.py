with open('CONTACT.in', mode='r', encoding='utf-8') as f:
    list_email = f.readlines()
    
list = list(set(email.rstrip('\n').lower() for email in list_email))
list.sort()

print(*list, sep='\n')