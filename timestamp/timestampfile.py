import requests
import hashlib
import time


status_url = 'http://www.proofofexistence.com/api/v1/status'
register_url = 'http://www.proofofexistence.com/api/v1/register'


class timestampfile:

    def __init__(self, File_Hash):
        self.File_Hash = File_Hash
    
    @property
    def request_timestamp (self):
        """
        using ProofOfExistence to register and make timestamp for a file
        @return: dictionary contains information about Bitcoin payment price and payment address. Returns -1 if failed.
        """
        returnval = {'pay_address':"", 'price':"", 'id':self.File_Hash}
        params = {'d': self.File_Hash}
        r = requests.post(status_url, data=params, timeout=10)
        if r.status_code != 200:
            return -1
        text = r.json()
        if text['success'] == False:
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
                returnval['pay_address'] = text['pay_address']
                returnval['price'] = text['price']
        return returnval

    
    def check_TimeStamp(self):
        """
        check whether the file has timestamp
        @return: dictionary contains information about timestamp status, timestamp time and transaction id. Returns -1 if failed.
        """
        File_Hash = self.File_Hash
        params = {'d': File_Hash}
        r = requests.post(status_url, data=params, timeout=10)
        returnval = {'timestamp': False, 'time': "", 'Transaction': "" }
        if r.status_code != 200:
            print("Error: HTTP Status Code " + r.status_code + ". " + "The request was not succeeded, expected staus code '200'. \n")
            return -1
        text = r.json()
        if text['success'] == False:
            return -1
        if text['success'] == True:
            r = requests.post(status_url, data=params)
            text = r.json()
            if text['status'] == 'pending':
                print("Your payment has been received. Please wait at least 1 minute for your payment to be certified. \n")
                time_out_count = 0
                while(text['status'] == 'pending'):
                    if time_out_count > 10:
                        print("Maximum 10 minute time limit exceeded. Transaction not confirmed. \n")
                        return -1
                    time_out_count += 1
                    time.sleep(60)
                    r = requests.post(status_url, data=params)
                    text = r.json()
                    if text['status'] == 'confirmed':
                        returnval['timestamp']=True
                    else:
                        return -1
            if text['status'] == 'confirmed':
                returnval['timestamp'] = True
        if returnval['timestamp'] == True:
            returnval['time']= text['txstamp']
            returnval ["Transaction"] = text['transaction']
        return returnval