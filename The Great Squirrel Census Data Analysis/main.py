import pandas 

data = pandas.read_csv("squirel_dataset.csv")

gray_count = (data["Primary Fur Color"] == 'Gray').sum()
cinnamon_count = (data["Primary Fur Color"]=='Cinnamon').sum()
black_count = (data["Primary Fur Color"]=='Black').sum()

squirel_data = {
    "FUR COLOR": ["Gray", "Cinnamon", "Black"],
    "COUNT": [gray_count, cinnamon_count, black_count]
}

processed_data = pandas.DataFrame(squirel_data)
processed_data.to_csv("squirrel_count.csv")
   
