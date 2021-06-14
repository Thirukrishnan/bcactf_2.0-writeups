														Secure Zip

Gerald lost his homework in this zip file. He needs to extract his homework or else he fails CTF101.

Solution:

In this we have to basically crack a zip file to read its contents.

So for this we use a tool called fcrackzip.

We can get it from package manager apt (for debian )

sudo apt-get install -y fcrackzip

Once we get it we can crack the chall.zip file by the command:

cmd:fcrackzip -b -D -p /usr/share/wordlists/rockyou.txt -u chall.zip

Reading the flag.txt we get

FLAG:bcactf{cr4ck1ng_z1p_p455w0rd5_15_fun_a12ca37bdacef7}
