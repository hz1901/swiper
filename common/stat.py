'''系统状态码'''

OK = 0
SMSErr = 1000   # 发送验证码错误
VcodeExpired = 1001 # 验证码已过期
VcodeErr = 1002  # 证码错误
LoginRequired = 1003 # 需要用户登陆
UserDataErr = 1004 # 用户信息错误
ProfileDataErr = 1005 #交友信息错误