import requests
import hashlib
import time


status_url = 'http://www.proofofexistence.com/api/v1/status'
register_url = 'http://www.proofofexistence.com/api/v1/register'


def TimeStamp(File_Hash):
    """
    Timestamps a file by sending a hashed document/collection to proofofexistence.com
    after paying the minimum BTC value.  Success entry is either True or False. 
    If False, then it is possible that File_Hash is not registered at proofofexistence.
    If True, then the 'status' entry is either 'registered', 'pending' or 'confirmed':
        If entry is 'registered' then payment needs to be made.
        If entry is 'pending' then payment has been made and is awaiting entry into the blockchain to confirm transaction.
        If entry is 'confirmed' then payment for that particular digest has been made.
    
    @param File_Hash A SHA256 Hash
    @return Returns a bitcoin transaction id (txid). Returns -1 if failed.
    """
    params = {'d': File_Hash}
    r = requests.post(status_url, data=params, timeout=10)
    
    #Check if HTTP status code is (200 OK).
    if r.status_code != 200:
        print("Error: HTTP Status Code " + r.status_code + ". " 
            + "The request was not succeeded, expected staus code '200'. \n")
        return -1
    
    text = r.json()
    if text['success'] == False:
        
        #Register nonexistent File_Hash
        if text['reason'] == 'nonexistent':
            r = requests.post(register_url, data=params)
            text = r.json()
            if text['success'] == False:
                    print("Opps, failed to register digest! \n")
                    return -1
             
    if text['success'] == True:
        r = requests.post(status_url, data=params)
        text = r.json()
        if text['status'] == 'registered':
                BTC_price = text['price']
                Pay_Address = text['pay_address']
                print("Please pay a minimum value of " + str(BTC_price) + " satoshis to address " 
                    + "'" + Pay_Address + "'" + "\n")
                input("If you have submitted your payment. Press Enter to continue...")
        if text['status'] == 'pending':
            print("Your payment has been received. Please wait at least 1 minute for your payment to be certified. \n")
            
            #Payment needs at least 1 minute to confirm the transaction. Set 10 minute time limit.
            time_out_count = 0
            while(text['status'] == 'pending'):
                if time_out_count > 10:
                    print("Maximum 10 minute time limit exceeded. Transaction not confirmed. \n")
                    break
                time_out_count += 1
                time.sleep(60)
                r = requests.post(status_url, data=params)
                text = r.json()
            if text['status'] == 'confirmed':
                txid = text['transaction']
                txstamp = text['txstamp']
                print("Done, confirmed documents! \n"  + "Bitcoin transaction id (txid): " + txid 
                    + "\n"+ "Transaction timestamp: " + txstamp + "\n")
                return txid
            
        elif text['status'] == 'confirmed':
            print("Document already confirmed! \n")
            return(text['transaction'])
        else:
            #File_Hash has already been registered and no payment has been made.
            print("A payment was not recieved. Please submit a payment in order to perform a timestamp. \n")
            
    #printing reponse object for debugging purposes        
    print(r.json())
    return -1
