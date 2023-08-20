import pandas as pd

fruit_sales = pd.DataFrame(columns=["Apples", "Bananas"])

fruit_sales = pd.DataFrame({'Apples': [35, 41],
                           'Bananas' : [21, 34]},
                          index=['2017 Sales', '2018 Sales'])

write_fruit_sales = fruit_sales.to_csv(r'C:\Users\jomuf\Documents\CODE KENTUCKY PROJECTS\DLGITHF\fruit-sales-exercise-JodieMullins\fruit.csv')