import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
anime = pd.read_csv("Data from Internet blog.csv")
pd.options.display.float_format = '{:,.2f}'.format

#Данные по непрерывным переменным
print("\n",'{:-^50}'.format('ДАННЫЕ ПО НЕПРЕРЫВНЫМ ПЕРЕМЕННЫМ'),"\n")

print(anime[["Дочитки","СВД","ПД","Просмотры","Показы","CTR","Комменты","Подписки","Лайки"]].mean())
print("\n")
print(anime[["Дочитки","СВД","ПД","Просмотры","Показы","CTR","Комменты","Подписки","Лайки"]].median())
print("\n")

print(anime.agg({"Дочитки":['min', 'max', 'median', 'skew'],"СВД":['min', 'max', 'median', 'skew'],"ПД":['min', 'max', 'median', 'skew'],"Подписки":['min', 'max', 'median', 'skew']}))
print("\n")
print(anime.agg({"CTR":['min', 'max', 'median', 'skew'],"Показы":['min', 'max', 'median', 'skew'],"Комменты":['min', 'max', 'median', 'skew'],"Лайки":['min', 'max', 'median', 'skew']}))

#Категоризация данных
print("\n",'{:-^50}'.format('КАТЕГОРИЗАЦИЯ ДАННЫХ'),"\n")

anime['Ур. дочиток'] = pd.cut(anime['Дочитки'], bins=[0,5200,9500,23000,54000], labels=['Низкий','Средний',"Высокий","Очень высокий"])
anime['Дл. чтения'] = pd.cut(anime['СВД'], bins=[0,57,77,100,173], labels=['Низкая','Средняя',"Высокая","Лонгрид"])
anime['Ур. CTR'] = pd.cut(anime['CTR'], bins=[0,5,7,10,13], labels=['Низкий','Средний',"Высокий","Бенгер"])
anime['Ур. вовлеч.'] = pd.cut(anime['Лайки'], bins=[0,150,300,450,1000], labels=['Низкий','Средний',"Высокий","Очень высокий"])

print(anime[["Тип","Ур. дочиток",'Дл. чтения',"Ур. CTR",'Ур. вовлеч.']].describe())

#Данные по категории "Тип"
print("\n",'{:-^50}'.format('ДАННЫЕ ПО КАТЕГОРИИ ТИП'),"\n")

with pd.option_context("display.max_columns", None): 
 print(anime[["Тип", "Дочитки"]].groupby("Тип").describe())
print(anime[["Тип", "Дочитки"]].groupby("Тип").median())

print(anime[["Тип", "CTR"]].groupby("Тип").describe())
print(anime[["Тип", "CTR"]].groupby("Тип").median())

print(anime[["Тип", "СВД"]].groupby("Тип").describe())
print(anime[["Тип", "СВД"]].groupby("Тип").median())

print(anime[["Тип", "Лайки"]].groupby("Тип").describe())
print(anime[["Тип", "Лайки"]].groupby("Тип").median())

#Данные по категории "Ур. дочиток"
print("\n",'{:-^50}'.format('ДАННЫЕ ПО КАТЕГОРИИ УРОВЕНЬ ДОЧИТОК'),"\n")

with pd.option_context("display.max_columns", None): 
 print(anime[["Ур. дочиток", "Дочитки"]].groupby("Ур. дочиток").describe())
print(anime[["Ур. дочиток", "Дочитки"]].groupby("Ур. дочиток").median())

print(anime[["Ур. дочиток", "Подписки"]].groupby("Ур. дочиток").describe())
print(anime[["Ур. дочиток", "Подписки"]].groupby("Ур. дочиток").median())

print(anime[["Ур. дочиток", "CTR"]].groupby("Ур. дочиток").describe())
print(anime[["Ур. дочиток", "CTR"]].groupby("Ур. дочиток").median())

with pd.option_context("display.max_columns", None): 
 print(anime[["Ур. дочиток", "Показы"]].groupby("Ур. дочиток").describe())
print(anime[["Ур. дочиток", "Показы"]].groupby("Ур. дочиток").median())

print(anime[["Ур. дочиток", "Лайки"]].groupby("Ур. дочиток").describe())
print(anime[["Ур. дочиток", "Лайки"]].groupby("Ур. дочиток").median())

#Данные по категории "Дл. чтения"
print("\n",'{:-^50}'.format('ДАННЫЕ ПО КАТЕГОРИИ ДЛИТЕЛЬНОСТЬ ЧТЕНИЯ'),"\n")

print(anime[["Дл. чтения", "СВД"]].groupby("Дл. чтения").describe())
print(anime[["Дл. чтения", "СВД"]].groupby("Дл. чтения").median())

print(anime[["Дл. чтения", "Комменты"]].groupby("Дл. чтения").describe())
print(anime[["Дл. чтения", "Комменты"]].groupby("Дл. чтения").median())

#Данные по категории "Ур. CTR"
print("\n",'{:-^50}'.format('ДАННЫЕ ПО КАТЕГОРИИ УРОВЕНЬ CTR'),"\n")

print(anime[["Ур. CTR", "CTR"]].groupby("Ур. CTR").describe())
print(anime[["Ур. CTR", "CTR"]].groupby("Ур. CTR").median())

with pd.option_context("display.max_columns", None): 
 print(anime[["Ур. CTR", "Показы"]].groupby("Ур. CTR").describe())
print(anime[["Ур. CTR", "Показы"]].groupby("Ур. CTR").median())

#Данные по категории "Ур. вовлеч."
print("\n",'{:-^50}'.format('ДАННЫЕ ПО КАТЕГОРИИ УРОВЕНЬ ВОВЛЕЧЕННОСТИ'),"\n")

print(anime[["Ур. вовлеч.", "Лайки"]].groupby("Ур. вовлеч.").describe())
print(anime[["Ур. вовлеч.", "Лайки"]].groupby("Ур. вовлеч.").median())

print(anime[["Ур. вовлеч.", "Комменты"]].groupby("Ур. вовлеч.").describe())
print(anime[["Ур. вовлеч.", "Комменты"]].groupby("Ур. вовлеч.").median())

print(anime[["Ур. вовлеч.", "ПД"]].groupby("Ур. вовлеч.").describe())
print(anime[["Ур. вовлеч.", "ПД"]].groupby("Ур. вовлеч.").median())

count = anime['Название'].str.split().apply(len).value_counts()
count.index = count.index.astype(str) + ' слов:'
count.sort_index(inplace=True)
print(count)

#ВИЗУАЛИЗАЦИЯ ДАННЫХ ПРИ ПОМОЩИ SEABORN

sns.set_style('whitegrid')

#Диаграммы распределения непрерывных переменных

x = np.log10(anime['Дочитки'])
sns.distplot(x)
plt.title("ПЛОТНОСТЬ РАСПРЕДЕЛЕНИЯ ДОЧИТЫВАНИЙ")
plt.xlabel('Дочитывания')
plt.figure() 

sns.distplot(anime['Дочитки'])
plt.title("ПЛОТНОСТЬ РАСПРЕДЕЛЕНИЯ ДОЧИТЫВАНИЙ")
plt.xlabel('Дочитывания')
plt.figure() 

sns.jointplot(x='Показы', y='CTR', data=anime, kind='hex')
plt.subplots_adjust(top=0.93)
plt.suptitle('СОВМЕСТНОЕ РАСПРЕДЕЛЕНИЕ ПОКАЗОВ И CTR')
plt.figure()

sns.jointplot(x='Показы', y='CTR', data=anime, kind='reg')
plt.subplots_adjust(top=0.93)
plt.suptitle('РЕГРЕССИЯ ПОКАЗОВ И CTR')
plt.figure() 

sns.heatmap(anime[['Дочитки',"Лайки","Подписки","Комменты","CTR"]].corr(),cmap='coolwarm', annot= True)
plt.subplots_adjust(top=0.9)
plt.suptitle('ТЕПЛОВАЯ КАРТА')
plt.figure() 

#Диаграммы размаха категориальных переменных

sns.boxplot(x="Ур. дочиток", y="CTR", data=anime, hue='Тип', palette='coolwarm'); 
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАЗМАХА ДОЧИТЫВАНИЙ')
plt.figure()

sns.boxplot(x="Дл. чтения", y="Лайки", data=anime, hue='Тип', palette='coolwarm'); 
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАЗМАХА ВРЕМЕНИ ЧТЕНИЯ')
plt.figure() 

sns.violinplot(x="Ур. CTR", y="Показы", data=anime, hue='Тип', palette='coolwarm'); 
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАЗМАХА CTR')
plt.figure() 

sns.violinplot(x="Ур. вовлеч.", y="ПД", data=anime, hue='Тип', palette='coolwarm'); 
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАЗМАХА ВОВЛЕЧЕННОСТИ')
plt.figure() 

#Диаграммы рассеивания категориальных переменных

sns.swarmplot(x="Ур. дочиток", y="СВД", data=anime, hue='Тип', palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАССЕИВАНИЯ ДОЧИТЫВАНИЙ')
plt.figure() 

sns.swarmplot(x="Дл. чтения", y="Лайки", data=anime, hue='Тип', palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАССЕИВАНИЯ ВРЕМЕНИ ЧТЕНИЯ')
plt.figure()

sns.swarmplot(x="Ур. CTR", y="Показы", data=anime, hue='Тип', palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАССЕИВАНИЯ CTR')
plt.figure()

sns.swarmplot(x="Ур. вовлеч.", y="ПД", data=anime, hue='Тип', palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА РАССЕИВАНИЯ ВОВЛЕЧЕННОСТИ')
plt.figure() 

#Диаграммы для агрегирования категориальных переменных

sns.barplot(x='CTR', y='Ур. дочиток', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА  СООТВЕТСВИЯ CTR И ДОЧИТЫВАНИЙ')
plt.figure() 

sns.barplot(x='СВД', y='Ур. CTR', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА  СООТВЕТСВИЯ ВРЕМЕНИ ЧТЕНИЯ И CTR')
plt.figure() 

sns.barplot(x='Комменты', y='Ур. вовлеч.', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА  СООТВЕТСТВИЯ КОММЕНТАРИЕВ И УРОВНЯ ВОВЛЕЧЕННОСТИ')
plt.figure() 

sns.barplot(x='Лайки', y='Дл. чтения', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДИАГРАММА СООТВЕТСВИЯ ЛАЙКОВ И ДЛИТЕЛЬНОСТИ ЧТЕНИЯ')
plt.figure() 

sns.countplot(x='Ур. дочиток', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('УРОВЕНЬ ДОЧИТЫВАНИЙ ПО ТИПУ ПУБЛИКАЦИИ')
plt.figure() 

sns.countplot(x='Дл. чтения', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('ДЛИТЕЛЬНОСТЬ ЧТЕНИЯ ПО ТИПУ ПУБЛИКАЦИИ')
plt.figure() 

sns.countplot(x='Ур. CTR', data=anime,hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('УРОВЕНЬ CTR ПО ТИПУ ПУБЛИКАЦИИ')
plt.figure() 

sns.countplot(x='Ур. вовлеч.', data=anime, hue='Тип',palette='coolwarm')
plt.subplots_adjust(top=0.9)
plt.suptitle('УРОВЕНЬ ВОВЛЕЧЕННОСТИ ПО ТИПУ ПУБЛИКАЦИИ')
plt.figure() 