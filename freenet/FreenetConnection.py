import fcp, uuid

class FreenetConnection:
    def __init__(self):
        self.fcpNode = fcp.FCPNode(host="localhost")
          
    '''
    Put a text file onto the freenode network
    
    @param filename - String that will be used for the KSK
                      or keyword-signed keys
    @param data - The text data to add to freenode
    @return - complete URI for the file
    '''
    def put(self, filename, data):
        uri= "KSK@" + filename+ uuid.uuid4().hex
        job = self.fcpNode.put(uri, data=data, mimetype="text/plain", async=True)
        if job.isComplete(): 
            print("this happens")
            return uri
        else:
            job.wait()
        return uri

    '''
    Retrieve a text file from the freenode network
    @param uri - the 'KSK@' prepended URI for the file on the network
    @return - The textual data 
    '''
    def get(self, uri):
        job = self.fcpNode.get(uri, asynch=True)
        #Note, this currently returns just the data
        #other info like header, completion time is stored in the
        #dictionary in job[2]
        return job[1]
