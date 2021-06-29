import ctypes
import win32com.client

cpStatus = win32com.client.Dispatch('CpUtil.cpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')

def check_creon_system():
	# 권리자 권한으로 프로세스 실행 여부
	if not ctypes.windll.shell32.IsUserAnAdmin():
		print('check_creon_system() : admin user -> FAILED')
		return False
	
	# 연결 여부 체크
	if cpStatus.IsConnect == 0: # 0 - 연결 끊킴 / 1 - 연결 정상
		print('check_creon_system() : connect to server -> FAILED')
		return False
	
	if cpTradeUtil.TradeInit(0) != 0:
		print('check_creon_system() - ERROR : cpTradeUtil ', cpTradeUtil.TradeInit(0), ' -> FAILED')
		return False
	
	return True

