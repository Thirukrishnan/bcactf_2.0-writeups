								 Easy RSA

As part of his CTF101 class, Gerald needs to find the plaintext that his teacher encrypted. Can you help him do his homework? ( It's definetely not cheating ;) )

In enc.txt we have

p:  251867251891350186672194341006245222227
q:  31930326592276723738691137862727489059
n:  8042203610790038807880567941309789150434698028856480378667442108515166114393
e:  65537
ct:  5247423021825776603604142516096226410262448370078349840555269847582407192135


Solution:

This is an easy RSA problem where we are given all the necessary values like p,q,n,e to decrypt.

I used dcode.fr for this challenge.
https://www.dcode.fr/rsa-cipher

If we give these values to the calculator we can get the flag:

FLAG:bcactf{RSA_IS_EASY_AFTER_ALL}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

								 Cipher Mishap

My Caeser-loving friend decided to send me a text file, but before sending it, his sister, who loves Caps Lock, tampered with the file. Can you help me find out what my friend sent me? Note: the answer must be wrapped in bcactf{}

The text file has:
126-Y, 113-N, 122-N, 130-N, 117-N, 107-N, 137, 114-N, 127-Y, 137, 113-Y, 104-N, 131-N, 110-N, 137, 105-Y, 110-N, 110-N, 121-Y, 137, 131-Y, 114-N, 112-N, 110-N, 121-N, 110-N, 125-N, 110-N, 137, 114-Y, 121-N, 126-N, 127-N, 110-N, 104-N, 107-N

Solution:

So first I tried to ignore the Y's and N's hence I separated the numbers.Then I used Cyberchef tool to find the base of these numbers.

http://icyberchef.com/

The Cyberchef is a excellent tool for solving various crypto challenges has it possess various encoding and encryption methods and their counter-part.

So trying to decode from different bases , I found readable characters with base 8(Octal).
VKRXOG_LW_KDYH_EHHQ_YLJHQHUH_LQVWHDG

They have also mentioned about Caesar so I tried bruteforcing the text with different shifts using the python code I wrote.

With shift 3 i got the text :SHOULD_IT_HAVE_BEEN_VIGENERE_INSTEAD

Now that Y and N makes sense the letters which have Y infront of them must be CAPS others in lower-case.Also we must add the bcactf{} to meet the flag format.

FLAG:bcactf{Should_iT_Have_BeeN_Vigenere_Instead}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

							       Slightly Harder RSA

Gerald's homework is getting trickier. He isn't being given the primes anymore. Help him find the plaintext!


The text file has:

n = 947358141650877977744217194496965988823475109838113032726009
e= 65537
ct=811950322931973288295794871117780672242424164631309902559564


Solution:

So in this challenge we are given only n and e.But it is possible to factorize n to get p and q in this case.
Again using the dcode.fr site we first have to find p and q from this n ,then use these same as Easy RSA chall to get flag.

p:	884666943491340899394244376743
q:	1070864180718820651198166458463 

FLAG:bcactf{rsa_factoring}

