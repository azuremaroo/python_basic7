import numpy as np
import pandas as pd

mynewsdf = pd.read_excel("newstitle.xlsx",index_col=0)
print(mynewsdf)
#
# # for item in mynewsdf['NewsTitle']:
# #     print(item)
# print(mynewsdf.loc[0,'NewsTitle'])
# import re
#
# result = re.findall('[ㄱ-힣]+', mynewsdf.loc[0,'NewsTitle'])
# print(result)
# res = ' '.join(result)
# print(res)
#
# mynewsdf.loc[0,'NewsTitle'] = res
# print(mynewsdf)