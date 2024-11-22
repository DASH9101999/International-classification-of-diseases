# import access_neo4j as neo4
import os
def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')
# verify connection

# neo4.verify_connection()

class Entity:
    def __init__(self, title, children ):
        self.title = title
        self.children = children

    def get_title(self):
        return self.title
    
    def get_children(self):
        return self.children
    
    def disp_entity(self):
        print(f'{self.title.upper()}')
        for i in sorted(self.children):
            print(f'        {i}')
    
    def wr_entity(self,file):
        file.write(f"{self.title}:"+'\n')
        for child in sorted(self.children):
            file.write(f"    {child.strip()}"+"\n")


# get data from txt file
data=[]
with open('relationships.txt','r' , encoding='cp437') as f:
    data = f.readlines()
    data= [x.strip() for x in data]
# f.close()


seperator='--->'
relationships_dict = {}
for line in data:
    title, children = line.strip().split(seperator)
    if title not in relationships_dict.keys():
        relationships_dict[title] = []
    relationships_dict[title].append(children)





def insert_data_to_entity(relationship):
    title = relationship
    children = relationships_dict[title]
    return Entity(title,children)

# create entities

Entities_list = []
for relationship in relationships_dict:
    Entities_list.append(insert_data_to_entity(relationship))



# add the entities to neo4j

# c=0
# for entity in entities:
#     father_entity = entity.title.strip()
#     for child in entity.children:
#         child_entity = child.strip()
#         neo4.edit(f'''
#             MERGE (child:ENTITY {{name: "{child_entity}"}})
#             MERGE (parent:ENTITY {{name: "{father_entity}"}})
#             MERGE (child)-[:IS_CHILD]->(parent)
#         ''')
#     c+=1
#     print(c)



# search in entities 
def search(text, Entities_list):
    c=0
    for entity in Entities_list:
        if text in entity.get_title():
            c+=1
            print(f'{c}. ',end="")
            entity.disp_entity()
            print ('----------------------------------------------------------------')
        else:
            for x in entity.children:
                if text in x:
                    c+=1
                    print(f'{c}. ',end="")
                    entity.disp_entity()
                    print ('----------------------------------------------------------------')
    print(f'''
    
       

        {c} result founded
''')
        

print ('----------------------------------------------------------------')
print ('----------------------------------------------------------------')





    # neo4.edit(f'''
    #     MERGE (child:ENTITY {{name: "{i.strip()}"}})
    #     MERGE (parent:ENTITY {{name: "{tle.strip()}"}})
    #     MERGE (child)-[:IS_CHILD]->(parent)
    # ''')
    
    # neo4.edit(f'MERGE(:ENTITY {{name: "{i.strip()}"}})-[:IS_CHILD]->(:ENTITY {{name: "{tle.strip()}"}})')


while True:
    text=input('search...').lower()
    clear()
    search(text,Entities_list)
    choice=input('Type "S" to search again...').lower()
    if choice=='s':
        clear()
        text=input('search...').lower().strip()
        search(text,Entities_list)
    else:
        clear()
        break