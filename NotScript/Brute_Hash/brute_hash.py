import hashlib
import sys

def md5_sha1(x):
    a = hashlib.sha1(x).hexdigest().encode('utf-8')
    return hashlib.md5(a).hexdigest()

def hash224(x):
    return hashlib.sha224(x).hexdigest()
	
def hash256(x):
    return hashlib.sha256(x).hexdigest()
	
def hash384(x):
    return hashlib.sha384(x).hexdigest()
	
def hash_sha1(x):
    return hashlib.sha1(x).hexdigest()

def hashmd5(x):
    return hashlib.md5(x).hexdigest()

def hash512(x):
    return hashlib.sha512(x).hexdigest()
	
def md5_3x(x):
    a = hashlib.md5(x).hexdigest().encode('utf-8')
    a = hashlib.md5(a).hexdigest().encode('utf-8')
    return hashlib.md5(a).hexdigest()

if __name__ == '__main__':
    all_str = 'abcdefghijklmnopqrstuvwxyz0123456789'

    # target = '6ef11bc47eadba4c9c4c44f1e4aaa84f'  # any target string
    if sys.argv[1:]:
        target = sys.argv[1]
    else:
        print('letak hash')
        target = input()

    # starting brute force
    for i in all_str:
        for j in all_str:
            for k in all_str:
                for l in all_str:
                    pw = i + j + k + l
                  # if md5_sha1(pw.encode()) == target:
                  # if hash224(pw.encode()) == target:
                  # if hash256(pw.encode()) == target:
                  # if hash384(pw.encode()) == target:
                  # if hash512(pw.encode()) == target:
                    if hash_sha1(pw.encode()) == target:
                  # if hashmd5(pw.encode()) == target:
                  # if md5_3x(pw.encode()) == target:
                        print(pw)
