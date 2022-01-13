from brownie import Bookstore, accounts, network, config
def main():
        dev1=accounts.add(config['wallets']['from_key']) 
        dev2=accounts.add(config['wallets']['from_key2'])
        print (network.show_active())
        book_store=Bookstore[len(Bookstore)-1]
        print(book_store)
        TokenId=book_store.tokenCounter ()
        book_store.Approve('0xeC5c3E3541D469535DCC0E62Add1128039fE82Dd', {"from":dev1})
        book_store.purchaseFromAuthor (TokenId,20,{ "from":dev2})