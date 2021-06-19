								Countdown Timer

Get the flag once the countdown timer reaches zero! However, the minimum time you can set for the countdown is 100 days, so you might be here for a while.  

http://web.bcactf.com:49154/


Solution :

Viewing the source code we can see they have used javascript to build that timer and minimum time we can set is 100 days.

Since they have used js once we get the source its possible to modify it in the browser (bcoz js is client side rendered).

So start the countdown and go to the console(Ctrl+Shift+I) and type time=0 which stops the timer.

FLAG:bcactf{1_tH1nK_tH3_CtF_w0u1D_b3_0v3r_bY_1O0_dAy5}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
								Home Automation
								   75 points
								   
Check out my super secure home automation system! No, don't try turning the lights off...

◇ http://web.bcactf.com:49155/  

Solution:
When we login as guest we see a lights on button when we click it we get a message : 

You must be admin to turn off the lights. Currently you are "vampire".

After this when we check for the cookies we see:

user:vampire

Then if we change the cookie user to admin and click on lights on we get the flag:

user: admin

FLAG: bcactf{c00k13s_s3rved_fr3sh_fr0m_th3_smart_0ven_cD7EE09kQ}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
								Movie-Login-1
								 100 points
								 
I heard a new movie was coming out... apparently it's supposed to be the SeQueL to "Gerard's First Dance"? Is there any chance you can help me find the flyer? 

◇ http://web.bcactf.com:49160/  

Solution:
Reading the statement itself we could find its SQL injection and this one is a trivial one.
In the login page both the username and password column is vulnerable to the SQL injection.
I used the username column to get the flag.
						
username:	' or 1=1 -- -;
password:anything or leave it blank

FLAG:bcactf{s0_y0u_f04nd_th3_fl13r?}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
								Movie-Login-2
								 150 points
								 
It's that time of year again! Another movie is coming out, and I really want to get some insider information. I heard that you leaked the last movie poster, and I was wondering if you could do it again for me?    

◇ denylist.json  
◇ http://web.bcactf.com:49153/  

Solution:
In this its the same login page with same vulnerability but this time certain characters will be filtered out when we use them on the username or password prompts.
These characters were given in the denylist.json file.

 1,0,/,=
 
So this time we have to inject using different SQL statement.The payload i used was

username:	' or 2 is 2 -- -; (is operator is same as =, it checks whether two values are same )
password:

FLAG:bcactf{h0w_d1d_y0u_g3t_h3r3_th1s_t1m3?!?}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
								Movie-Login-3
								 200 points
								 
I think the final addition to the Gerard series is coming out! I heard the last few movies got their poster leaked. I'm pretty sure they've increased their security, though. Could you help me find the poster again?    

◇ denylist.json  
◇ http://web.bcactf.com:49162/  

Solution:
This is similar to Movie-Login 2 but we are given different deny list.

and,1,0,true,false,/,*,=,xor,null,s,<,>


username:	' or ‘a’ like ‘a’ -- -; ( like operator is used to compare characters or strings ‘a’ represents a character)
password:

FLAG:bcactf{gu3ss_th3r3s_n0_st0pp1ng_y0u!}

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
								Agent Gerald
								 125 points
								 
Agent Gerald is a spy in SI-6 (Stegosaurus Intelligence-6). We need you to infiltrate this top-secret SI-6 webpage, but it looks like it can only be accessed by Agent Gerald's special browser...  
  
◇ http://web.bcactf.com:49156/  

Solution:
In this challenge we have to impersonate Agent Gerald to retrieve the flag.Since we are given we need special browser and the chall itself says Agent it can be User-Agent spoofing.
User-Agent header in http request tells the info about our browser and other specs.
To spoof this we can use Burp-Suite tool.But I thought of using ou browser itself.

I will explain for Chrome, for other browsers use this link :https:// www.searchenginejournal.com/change-user-agent/368448/#close

In chrome Right-Click -> Inspect -> Click on the 3 dots on top right corner -> More tools -> Network Conditions -> Uncheck Use browser default ->Add custom User-Agent value to Gerald.
Now refreshing the page we get the flag.

FLAG: bcactf{y0u_h@ck3d_5tegos@urus_1nt3lligence}

Remember to change this value to default after the challenge....
