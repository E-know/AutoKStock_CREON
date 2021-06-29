import win32com.client


class account_info():
	
	def __init__(self):
		self.__CpTd6033 = win32com.client.Dispatch('CpTrade.CpTd6033')
		self.__CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
		self.__CpTdUtil.TradeInit()  # Test 용 끝나면 삭제
		
		self.balance = None
		self.profit_rate = None
		self.profit_amount = None
		self.share = {}
		self.account_number = self.__CpTdUtil.AccountNumber[0]
		
		self.__get_account_info()
	
	def __get_account_info(self):
		self.__CpTd6033.SetInputValue(0, self.account_number)
		self.__CpTd6033.SetInputValue(1, '10')
		self.__CpTd6033.SetInputValue(2, 50)
		self.__CpTd6033.BlockRequest()
		
		self.balance = self.__CpTd6033.GetHeaderValue(9)
		self.profit_rate = self.__CpTd6033.GetHeaderValue(8)
		self.profit_amount = self.__CpTd6033.GetHeaderValue(4)
		
		receive_data_num = self.__CpTd6033.GetHeaderValue(7)
		
		for i in range(receive_data_num):
			name = self.__CpTd6033.GetDataValue(0, i)
			code = self.__CpTd6033.GetDataValue(12, i)
			share_num = self.__CpTd6033.GetDataValue(15, i)
			price = self.__CpTd6033.GetDataValue(18, i)
			
			self.share[code] = {'name' : name, 'amount': share_num, 'price': price}
			
def Test():
	a = account_info()
	print(a.balance)
	print(a.profit_rate)
	print(a.profit_amount)
	for key in a.share.keys():
		print(a.share[key])
	
# Test()
