#/use/local/bin/python
# coding: utf-8

import sys, os, sha

open("access", "w")

def signUp():
	print "Please input user information"
	user_info = []	#사용자 아이디를 제외한 정보를 저장할 리스트

	id_plain = raw_input("User ID : ")	#사용자 아이디 저장
	acc = open("access", "r")
	user_id = []	#파일에 저장된 사용자 아이디 목록을 저장할 리스트

	for line in acc:
		user_id.append(line.split()[0].strip(':'))

	while id_plain in user_id:
		print "Sorry, the entered ID is already used"
		yn = raw_input("Are you want to re-input your id? (Y / N)")
		if yn == 'Y' or yn == 'y':
			id_plain = raw_input("User ID : ")
		elif yn == 'N' or yn == 'n':
			print "Return to main menu"
			return 0

	password_plain = raw_input("User Password : ")
	password_encrypted = sha.new(password_plain).hexdigest()
	user_info.append(password_encrypted)
	
	user_info.append(raw_input("User Name : "))
	user_info.append(raw_input("User School : "))
	acc = open("access", "a+")
	
	print id_plain
	print user_info
	
	acc.writelines(id_plain + ": " + ", ".join(user_info) + '\n')
	
def signIn():
	print "Please input ID and Password"
	id_plain = raw_input("User ID : ")
	acc = open("access", "r")
	user_id = []
	user_pw = []
	for line in acc:
		user_id.append(line.split(":")[0])
		user_pw.append(line.split(":")[1].strip().split(", "))

	user_acc = dict(zip(user_id, user_pw))
	
	print user_acc
	
	while (id_plain in user_id) == False:
		print "Sorry, you are not registered member."
		yn = raw_input("Are you want to re-input your id? (Y / N)")
		if yn == 'Y' or yn == 'y':
			id_plain = raw_input("User ID : ")
		elif yn == 'N' or yn == 'n':
			print "Return to main menu"
			return 0
	password_plain = raw_input("User Password : ")
	password_encrypted = sha.new(password_plain).hexdigest()
	
	while (password_encrypted == user_acc[id_plain][0]) == False:
		print "Sorry, the entered password is not correct"
		yn = raw_input("Are you want to re-input your password? (Y / N)")
		if yn == 'Y' or yn == 'y':
			password_plain = raw_input("User Password : ")
			password_encrypted = sha.new(password_plain).hexdigest()
		elif yn == 'N' or yn == 'n':
			print "Return to main menu"
			return 0
	print "Hello", id_plain + ":", user_acc[id_plain][1:], "!"

def Quit():
	return 0

menu = {1 : signUp, 2 : signIn, 3 : Quit}

def selMenu():
	sel = 0
	print "Welcome to Our Service"
	
	print " 1. Sign Up \n 2. Sign in \n 3. Quit \n\n"
	sel = int(raw_input(">> please select menu : "))
	
	while(sel > 3 or sel < 1):
		print("\n Please input 1 to 3! \n")
		sel = int(raw_input(">> please select menu : "))

	return sel

sel = 0

while sel != 3:
	sel = selMenu()
	menu[sel]()

