###null

def ifnull0(df):
	if df.isna().sum() > 0:
		df = df.fillna(0)

