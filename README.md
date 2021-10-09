# gamblers-fallacy
how gamblers get tricked in the roulette game<br/>
<br/>
file: gamblers-fallacy.py<br/>
<br/>
## Gambler's Fallacy<br/>
It's a logical misunderstanding that previuos events can influence future events. In 1913 in a Casino in Monte Carlo there was a streak with black numbers in roulette. After people noticed that black came about 15 times in a row, they started to put more money on red thinking that the streak should end. But black came 26 times in a row overall. People lost millions.
<br/>
We want to demonstrate the thinking of the gamblers with a simple python script. We simulate simple coinflips with a 50% chance to occure. However, in roulette there is a 0 which is neither black or red. In fact the chance to hit black or red is 48,6%. But for the sake of understanding the disaster we leave it with 50%.<br/>
<br/>
We simulate 100 millions of coinflips and as a result we get the information how many times a certain streak appeared. In my example the highest streak is 29 which occured once.<br/>
```
sum of coinflips: 100,000,000
1 in a row:  24995784
2 in a row:  12499249
3 in a row:  6252952
4 in a row:  3124815
5 in a row:  1560560
6 in a row:  781009
7 in a row:  390406
8 in a row:  195619
9 in a row:  98403
10 in a row:  48859
11 in a row:  24521
12 in a row:  12005
13 in a row:  6075
14 in a row:  3030
15 in a row:  1584
16 in a row:  783
17 in a row:  415
18 in a row:  217
19 in a row:  96
20 in a row:  55
21 in a row:  33
22 in a row:  17
23 in a row:  8
24 in a row:  3
25 in a row:  0
26 in a row:  1
27 in a row:  0
28 in a row:  0
29 in a row:  1
```
The problem is that the gambler thinks obviously the higher the streak the lesser the chance that the ball will fall on the same color.<br/>
This is the reason why the casinos earn so much money. The previous events are in the past. With each game the chances are exact the same, like above 48,6% or in our example 50%. We get tricked by our brain with the results like above saying:"it's not possible that the same color appears forever". And there is a truth behind it. If you bet with somebody that the same color will appear 29 times in a row from now on, the chance that to happen is very low. Please, don't get tricked and understand that which each new game, the chances are always the same as before.
