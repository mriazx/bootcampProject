import hashlib

def md5_hash(s):
  return hashlib.md5(s.encode()).hexdigest()

def sha1_hash(s):
  return hashlib.sha1(s.encode()).hexdigest()

def sha256_hash(s):
  return hashlib.sha256(s.encode()).hexdigest()


def hash_iteration(s,slt,n):
  salted_text = s + slt
  for i in range(n):
    if i == 0:
      hash = hashlib.md5(salted_text.encode()).hexdigest()
    else:
      hash = hashlib.md5(hash.encode()).hexdigest()
  return hash


if __name__ == "__main__":

  text = "This is python and network security bootcamp project."

  salt = "s@lT"

  print (md5_hash(text))
  print (sha1_hash(text))
  print (sha256_hash(text))
  print (hash_iteration(text,salt,5))
