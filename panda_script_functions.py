# Would gathering functions into classes be of any benefit?

def set_dirs

def set_logs

def log_events

def set_login():
    login = raw_input("nbkid: ")
    return login

def set_password():
    print('Please enter corresponding password: ')
    pass = getpass.getpass()
    return pass

def access_message(when):
    if when == 'before':
        print('We will attempt access of the REST Confluence API using your login.')
    elseif when == 'during':
        print('We are now accessing REST Confluence API using your 
    elseif when == 'after':
        print('We are now accessing REST Confluence API using your 
    else:
        print('Input parameter *when* of function *access_message* not in scope: ' + when) # Exception??
    

def curl2pycurl


# http://stackoverflow.com/questions/1630706/best-practice-in-python-for-return-value-on-error-vs-success
class IntersectException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def intersect_two_lists(self, list1, list2):
    if not list1: raise IntersectException("list1 must not be empty.")
    if not list2: raise IntersectException("list2 must not be empty.")

    #http://bytes.com/topic/python/answers/19083-standard
    return filter(lambda x:x in list1,list2)