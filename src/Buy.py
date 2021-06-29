import win32com.client

CpTd = win32com.client.Dispatch('CpTrade.CpTd0311')

def buy_Stock(code, acc):
	
	setInputValue(CpTd, '2', acc, )
	


def setInputValue(obj, *values):
	for i, val in enumerate(values):
		obj.SetInputValue(i, val)