def describe_city(city_name, nation = 'China'):
	print(city_name.title() + " is in " + nation.title() + ".")
	
describe_city('qingdao')
describe_city('beijing')
describe_city('dongjing', 'japan')