import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
rannlab_url = "https://rannlab.com/"
text=input("Welcome to rannlab technology please tell me how can i help you")
service_url="https://rannlab.com/services/"
aboutus_url="https://rannlab.com/about-us/"
solution_url="https://rannlab.com/solutions/"
thinking_url="https://rannlab.com/latest-thinking/"
thinking_url="https://rannlab.com/latest-thinking/"
portfolio_url="https://rannlab.com/portfolio//"
bloglist_url="https://rannlab.com/blog-list/"
contactus_url="https://rannlab.com/contact-us/"
a=[]
file = open("myfile.txt","w")
L = [""]

# i assigned ["This is Lagos \n","This is Python \n","This is Fcc \n"] to #variable L, you can use any letter or word of your choice.
# Variable are containers in which values can be stored.
# The \n is placed to indicate the end of the line.



while(text!="thanks"):
  if(text=="service" or text in a):
    article = requests.get(service_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    print("hello")
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
      parents_list=[]
      for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
      parents_list
      parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
      parent_element_list.reverse()
      parent_hierarchy = ' -> '.join(parent_element_list)
  
      p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
      if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
   
  elif(text=="aboutus" or text in a):
    article = requests.get(aboutus_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
      parents_list=[]
      for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
      parents_list
      parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
      parent_element_list.reverse()
      parent_hierarchy = ' -> '.join(parent_element_list)
  
      p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
    if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
    
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
  elif(text=="solution" or text in a):
    article = requests.get(solution_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
      parents_list=[]
      for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
      parents_list
      parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
      parent_element_list.reverse()
      parent_hierarchy = ' -> '.join(parent_element_list)
   
      p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
    if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
    
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
   
  elif(text=="contactus" or text in a):
    article = requests.get(contactus_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
      parents_list=[]
      for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
      parents_list
      parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
      parent_element_list.reverse()
      parent_hierarchy = ' -> '.join(parent_element_list)
  
      p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
    if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
   
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
  elif(text=="thinking" or text in a):
    article = requests.get(thinking_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    print("hello")
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
     parents_list=[]
     for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
    parents_list
    parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
    parent_element_list.reverse()
    parent_hierarchy = ' -> '.join(parent_element_list)
  
    p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
    if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
    
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
  elif(text=="bloglist" or text in a):
    article = requests.get(bloglist_url)
    articles = BeautifulSoup(article.content, 'html.parser')
    articles_body = articles.findAll('body')    
    p_blocks = articles_body[0].findAll('p')
    print("hello")
    p_blocks_df=pd.DataFrame(columns=['element_name','parent_hierarchy','element_text','element_text_Count'])
    for i in range(0,len(p_blocks)):
  
      parents_list=[]
      for parent in p_blocks[i].parents:
        Parent_id = ''
        try:
          Parent_id = parent['id']
        except:
          pass
        parents_list.append(parent.name + 'id: ' + Parent_id)
      parents_list
      parent_element_list = ['' if (x == 'None' or x is None) else x for x in parents_list ]
      parent_element_list.reverse()
      parent_hierarchy = ' -> '.join(parent_element_list)
  
      p_blocks_df=p_blocks_df.append({"element_name":p_blocks[i].name
                                  ,"parent_hierarchy":parent_hierarchy
                                  ,"element_text":p_blocks[i].text
                                  ,"element_text_Count":len(str(p_blocks[i].text))}
                                  ,ignore_index=True
                                  ,sort=False)
    
    if len(p_blocks_df)>0 :
        p_blocks_df_groupby_parent_hierarchy=p_blocks_df.groupby(by=['parent_hierarchy'])
        p_blocks_df_groupby_parent_hierarchy_sum=p_blocks_df_groupby_parent_hierarchy[['element_text_Count']].sum()            
        p_blocks_df_groupby_parent_hierarchy_sum.reset_index(inplace=True)            

    maxid=p_blocks_df_groupby_parent_hierarchy_sum.loc[p_blocks_df_groupby_parent_hierarchy_sum['element_text_Count'].idxmax()
                                                     ,'parent_hierarchy']

    merge_text='\n'.join(p_blocks_df.loc[p_blocks_df['parent_hierarchy']==maxid,'element_text'].to_list())
    print(merge_text)
    
    a.append(text)
    file.write(text)
    file.writelines(text)
    text=input()
  else:
     print("please wait a min we provide information to you")
     
     a.append(text)
     file.write(text)
     file.writelines(text)
     text=input()
file.close()
