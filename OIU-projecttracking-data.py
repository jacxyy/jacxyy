import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 用来绘图的，封装了matplot
# 要注意的是一旦导入了seaborn，
# matplotlib的默认作图风格就会被覆盖成seaborn的格式
import seaborn as sns       

from scipy import stats
from scipy.stats import  norm
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline  
pd.set_option('display.max_columns',None)

data_train = pd.read_excel("D:\\file\\OIUTRACKING\\TEST20220509.xlsx")#20220509的OIU项目信息
data_train['duration'].df.filter('Created Date'=).describe()
sns.distplot(data_train['duration'])

# 2 years Client
var = '2 years Client'
data = pd.concat([data_train['duration'], data_train[var]], axis=1)
fig = sns.boxplot(x=var, y="duration", data=data)
fig.axis(ymin=0, ymax=40)

# Service Type(服务类型)
plt.figure(figsize = [20,10],dpi=100 )
var = 'Service Type(服务类型)'
data = pd.concat([data_train['duration'], data_train[var]], axis=1)
ax = sns.boxplot(x=var, y="duration", data=data)
ax.axis(ymin=0, ymax=40)
ax.set_xticklabels(labels =['Autoimmune Diseases',
'FACS',
'GEMM',
'IO- Pre-clinical Biomarker / FACS',
'IO- Pre-clinical Biomarker / others',
'IO- Pre-clinical Biomarker / Pathology',
'IO-Clinical Bio-marker / FACS',
'IO-Clinical Bio-marker / Pathology',
'IO-CRISPR in vitro',
'IO-CRISPR in vivo',
'IO-Humanized',
'IO-In Vitro',
'IO-NHP',
'IO-others',
'IO-Rat Syngeneic',
'IO-syngeneic',
'Others',
'RGD',
'RGD-GEAM',
'RGD-GECL',
'RGD-GTS',
'RGD-NHP',
'TO- Pre-clinical Biomarker / FACS',
'TO- Pre-clinical Biomarker / others',
'TO- Pre-clinical Biomarker / Pathology',
'TO-CDX',
'TO-CDX/In vitro',
'TO-CDX/PDX',
'TO-CDX/PDX/In vitro',
'TO-Clinical Bio-marker / FACS',
'TO-Clinical Bio-marker / Pathology',
'TO-CRISPR in vitro',
'TO-CRISPR in vivo',
'TO-In vitro',
'TO-NHP',
'TO-Others',
'TO-PDX',
'TO-Rat Xenograft'
],rotation=90,fontsize=15)
ax
