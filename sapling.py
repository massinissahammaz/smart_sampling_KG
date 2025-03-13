import pandas as pd
df=pd.read_csv('data.csv')
length =0
sample_df=pd.DataFrame()
entity_set=set()
entities_added=set()
entities_to_deal_with=set()
entities_to_deal_with_copy=set()
for index ,row in df.iterrows():
    entity_set.add(row['Head'])
    entity_set.add(row['Tail'])
while entity_set:
    if length>50000:
        break
    else:
        if entities_to_deal_with_copy:
            entities_to_deal_with.update(entities_to_deal_with_copy)
        else:
            entities_to_deal_with.add(entity_set.pop)
        for entity in entities_to_deal_with:
            if length >50000:
                break
            else:
                if entity not in entities_added:
                    for index ,row in df.iterrows():
                        if row['Head']==entity:
                            pd.concat([sample_df,row],ignore_index=True)
                            entities_to_deal_with_copy.add(row['Tail'])
                            length+=1
                        else:
                            if row['Tail']==entity:
                                pd.concat([sample_df,row],ignore_index=True)
                                entities_to_deal_with_copy.add(row['Head'])
                                length+=1
                    entities_added.add(entity)
        
print(sample_df.shape)
