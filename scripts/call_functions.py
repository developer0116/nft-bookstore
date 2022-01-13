from brownie import Bookstore, network
	
def main():

	print(network.show_active())
	book_store=Bookstore [len (Bookstore) -1]
	print (book_store)
	TokenId=book_store.tokenCounter()
	print (TokenId)
	Title=book_store.TitleOfTheBook(TokenId)
	print("Title of the Book ", Title)
	Author=book_store.AuthorOfTheBook(TokenId)
	print("Author of the Book : ",Author) 
	TotalCopiesPublished=book_store.TotalCopiesOfTheBook (TokenId)
	print("Total copies of the book published are :", TotalCopiesPublished)
	Balance=book_store.balanceOf("0xeC5c3E3541D469535DCC0E62Add1128039fE82Dd",TokenId)
	print(Balance)