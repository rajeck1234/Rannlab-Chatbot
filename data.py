import csv
  
# Open file 
text="ac"
i=0
while(i<2):
 if(text in open('myfile.csv').read() ):
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
    print("True")
    i=i+1
 else:
    print("False")
    i=i+1
with open('myfile1.csv') as file_obj:
      

    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
  
    for row in reader_obj:
        if(text in row):
          print(row)
