from pyobjust import autoclass

NSString = pyobjus('NSString')
text = NSString.alloc().initWithUTF8String_('Hello world')
print text.UTF8String() # --> Hello world