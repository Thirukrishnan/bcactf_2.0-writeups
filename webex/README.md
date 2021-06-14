														Countdown Timer

Get the flag once the countdown timer reaches zero! However, the minimum time you can set for the countdown is 100 days, so you might be here for a while.

http://web.bcactf.com:49154/


Solution :

Viewing the source code we can see they have used javascript to build that timer and minimum time we can set is 100 days.

Since they have used js once we get the source its possible to modify it in the browser (bcoz js is client side rendered).

So start the countdown and go to the console(Ctrl+Shift+I) and type time=0 which stops the timer.

FLAG:bcactf{1_tH1nK_tH3_CtF_w0u1D_b3_0v3r_bY_1O0_dAy5}